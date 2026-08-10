# 3. Findings

Section 3.1 reports the principal result: the checks a benchmark uses to
validate itself cannot detect errors in its own reference solution, and in
practice the solvers find those errors instead. Section 3.2 uses the same eight
domains to measure how far three already-documented effects vary when the
domain changes. Section 3.3 reports two observations from a single domain.

Cross-domain comparisons are restricted to arms B and C, the two arms present
in every benchmark (§2.4, §4.2.5).

---

## 3.1 A benchmark cannot validate its own reference solution

The proposition in this section's title is true by definition and requires no
experiment: a procedure defined as a function of the reference solution cannot
have the reference solution as its subject. We state it because it appears not
to be acted on, and because the empirical work adds three things the
proposition does not supply — **(1)** a case demonstrating that the gap is not
merely formal, in which a defect passed all three checks a benchmark of this
kind carries; **(2)** a record of where such defects were in fact found, and by
what; and **(3)** the identification of a detector that operates outside the
closed loop. Readers persuaded of the proposition may skip to §3.1.2.

That benchmarks contain incorrect ground truth is established, and so is the use
of models to find it (§5.1). The claim here is narrower and concerns a class of
error those results do not cover: **not a sparse annotation error attached to an
instance, but a systematic error in the program that derives the reference.**
Such an error displaces every case on the same code path in the same direction,
which removes the correct majority that statistical detection depends on, and
survives re-annotation by anyone who re-derives the answer along the same
specified procedure.

### 3.1.1 The three checks are all defined in terms of the reference

A benchmark of this kind carries three checks, described in §2:

| Check | Definition |
|---|---|
| **Grader** | Compares a submission against the reference solution |
| **Calibration** | Recomputes the reference by hand and requires agreement |
| **Adversarial suite** | Corrupts the reference and requires the grader to reject the result |

Each is a function of the reference solution. The grader measures distance from
it. Calibration recomputes it by an independent route, but along the same
specified procedure. The adversarial cases are *generated from* it, so every
attack inherits whatever the reference assumes.

Consequently these checks can establish that a submission deviates from the
reference, and that the grader notices deviation. **None of them can establish
that the reference is right.** The situation is that of a ruler: measurements
can be shown consistent with its graduations, but an error in the graduations
is not observable through it.

There is a second consequence, which we did not see until it produced a defect
(§3.1.5, and again in §3.1.6). A benchmark has a fourth artefact — the **task statement** given to
the solver — and it is the only one *not* derived from the reference. By the
same argument, the three checks cannot detect a disagreement between the two
either. They can confirm that the reference is graded as the reference; they
cannot confirm that it answers the question that was asked. Where the ruler
analogy has the graduations wrong, this has the ruler measuring a different
quantity than the one requested, and reporting consistent values throughout.

### 3.1.2 The clearest instance

In the geotechnical benchmark (`jiban`), the reference solution integrated the
liquefaction potential index below the bottom of the borehole. For one hole with
a drilled length of 10.63 m, the deepest sublayer was extended to the standard
20 m limit:

```
  9.43 – 10.43 m   FL = 0.327   contribution  3.390
 10.43 – 20.00 m   FL = 0.262   contribution 16.908   ← below the hole bottom (10.63 m)
```

**16.9 of a reported total of 28.0 — 60 percent — came from depth that was
never drilled.** Corrected, the value falls from 27.965 to 11.756.

The defect passed all three checks, and for the same reason in each case:

- The **grader** compares to the reference, which contained the defect
- **Calibration** followed the reference implementation to a difference of zero
  across all eleven intermediate quantities, because the hand computation used
  the same integration limit
- The **adversarial suite** passed twelve of twelve, because each case is built
  by corrupting the reference and therefore carries the same limit

It was located by three solvers independently, none of which had access to the
reference. They had the borehole record, and the borehole record ends.

### 3.1.3 Fifteen defects; fourteen found by the solvers

Across three rounds of the customs benchmark (`kanzei`), fifteen defects were
found on the **examination** side — in the tasks, the supplied material, or the
validator — rather than in the answers.

| | Count |
|---|---|
| Total examination-side defects | **15** |
| Located by the solvers | **14** |
| Located by our calibration or adversarial suites | **1** |
| Confirmed as real on review | **14** (one solver report was mistaken) |

The tariff schedule parser was corrected four times. In the geotechnical
benchmark, a further four defects were reported by solvers in a single round,
all confirmed (§3.1.2 is the third of them).

A later round supplies a cleaner instance, because the defects were introduced
knowingly-in-form and unknowingly-in-fact. The `jiban` replication of §3.2.2 was
issued with a worked example in the instructions. That example carried three
errors, all ours: its quantities were labelled as one seismic case while their
values belonged to another, the path it gave for the input files did not match
where they were placed, and it typed a numeric identifier as a string. **All six
solvers reported the first; three reported the second; none reported the third,
which surfaced only when every submission scored zero** — the grader could not
match a string identifier to an integer one, and reported the submissions as
empty rather than as mistyped.

The third is the instructive one. The solvers had followed the specification
exactly; the specification was wrong; and the failure presented as six identical
total failures, which is the signature of an examination defect rather than a
solver defect. A grader that reports *why* it found nothing distinguishes these
two cases immediately, and ours did.

The first error had an effect we did not anticipate. The example's internal
inconsistency made its numbers unusable as data — and four of the six solvers
used it anyway, as an arithmetic check: the difference between its total and
effective stress fixes the unit weight of water at 9.8 rather than 9.81. Two
stated explicitly that they had been about to use 9.81 from memory. **A broken
example prevented an error of recall in the majority of runs**, which is not an
argument for broken examples but is a data point about where these systems take
their constraints from.

One earlier defect was an operator error and is recorded because the failure
mode generalises. The tariff data was maintained as two artefacts — a structured
file and a plain-text file — and only the structured file was regenerated when
the parser was fixed. The stale plain text, in which **318 tariff codes were
indistinguishable**, was distributed to solvers for three rounds. One solver's
own report states that it read sibling ordering by grepping the plain text, so
the defect reached the answers. *If a pipeline emits more than one artefact from
one source, it must not be possible to update one of them alone.*

### 3.1.4 Why the solvers, and not the checks

This distribution — 14 against 1 — is not incidental. It follows from §3.1.1.
The three checks are computed from the reference and are therefore blind in
exactly the direction where the reference is wrong. A solver is not: it receives
the raw inputs and the task statement, and *not* the answer key, so its route to
an answer is independent of the reference. Where the reference contains an
assumption the inputs contradict, the solver is positioned to notice and the
checks are not.

**Within the benchmark's own loop the subject under test was the only detector
that located reference defects at all.** With fifteen instances we cannot rank
detectors — the defects a solver finds are, by construction, the ones a solver
can find, and the single defect our own checks caught may belong to a class they
are good at. The claim is about what worked here, not about relative power. It
is bounded in a second way as well, which we record because we met it: a third
detector, external to that loop, located a defect that neither the checks nor
the solvers reached, and that the solvers were structurally unable to reach
(§3.1.8).

We know of no procedure internal to the benchmark that substitutes for it, and
we did not find one. §3.1.6 reports a mechanical check that covers one
already-diagnosed class of task-statement defect; it was written from a solver
report rather than ahead of one, and does not substitute.

The established external procedures do not substitute for it either, for
reasons specific to this class of error (§5.1). Confident learning and related
statistical methods locate instances where a model confidently disagrees with
the label, and depend on the errors being rare against a correct majority; a
systematic implementation defect has no such majority, and uniform
model-versus-reference disagreement is precisely what a benchmark is built to
read as the models being wrong. Human re-annotation does not reach it either:
re-deriving a liquefaction assessment means executing the standard over the
same borehole data, and a misreading of the standard's integration bounds is
reproduced as readily the second time as the first. What the solvers contributed
was neither statistic nor re-derivation but an observation about the instance's
own inputs — the borehole record ends before the integration does.

Two practical consequences follow. First, **solver reports about the task should
be collected and adjudicated as a matter of course**, not treated as noise or as
excuses; fourteen of ours were correct. Second, **defect counts should be
published**. A benchmark that reports no examination-side defects has either not
looked or is not saying, and there is at present no way for a reader to tell
which.

### 3.1.5 Two limits, found by replicating a task we thought was clean

The `kikai` replication reported in §3.2.3 was run to measure repeatability, not
to look for defects. It produced two results that bear on the argument above,
and both cut against it.

**A defect the solvers could not have reported.** All six runs scored 94.6 with
an identical per-question breakdown, losing the same 4.8 points at the same nine
of twenty-eight items. The graded question covers five fields — the form of the
tolerance zone, projected length, unit length, unit area shape, and material
modifiers. **Four of the five appear nowhere in the task statement or the answer
format.** Only one of those four has instances in this file, so the entire
deduction is the zone form: eight position tolerances whose zone is cylindrical
and one whose zone is spherical, returned as null by every run. The answer
format's worked example uses a flatness tolerance, which carries no diameter
symbol, so the example is structurally incapable of revealing that the field
exists. Six solvers, in two arms, using different methods — one reading the file
directly, one writing a parser — omitted it identically. They did not misread
anything. They answered what was asked.

This is an examination-side defect of the same kind as the fifteen in §3.1.3,
but it reached us by a different route. No solver reported it, and none could
have: a solver cannot report the omission of a field whose existence the
specification never discloses. It became visible only on scoring, as a constant
deduction shared by every submission.

**Our adversarial suite had already constructed this exact submission and
classified it as an attack.** The suite includes a case named
`evil_drop_zone_form`, which takes the reference and blanks that field to check
that the grader notices. It scores **94.6 out of 100, losing Q5** — the same
score, on the same question, that all six honest solvers received. The case is
recorded as passing, because the grader did notice.

The machinery worked exactly as designed. It knew the field was graded, and
proved that dropping it was penalised. What no part of it could know is that the
task statement never asked for the field, so the penalised submission was the
compliant one. **The suite had written down the correct answer to a question it
was not able to ask.**

This locates the gap precisely, and it is a sharper version of §3.1.1 than we
stated there. The grader, the calibration and the adversarial suite are all
functions of the reference, which is why none can detect an error *in* the
reference. But the **task statement is not a function of the reference** — it is
the one artefact in the benchmark written independently of it — and by the same
argument, none of the three can detect a disagreement *between* the two. A
benchmark can be internally consistent to the last decimal place and still be
grading answers to a question it did not ask.

**The detector in §3.1.4 has a blind spot that is the exact complement of the
checks' blind spot** — the checks cannot see an error inside the reference, and
the solvers cannot see an error in what the reference asks for but the task does
not. Neither covers the other. What located this one was neither: it was the
pattern of six identical scores, which is available only under replication, and
replication is what §4.4 lists as the series' weakest dimension.

**An external check value that does not settle the reference.** The `kikai`
input is a NIST conformance test file, and NIST embeds its own expected counts in
it as `INTEGER_REPRESENTATION_ITEM` entities: 28 geometric tolerances, 4
composite tolerances, 6 datums, 6 datum targets, 67 semantic PMI elements. This
is the closest thing to a solution for §3.1.1 that the series encountered — the
data provider stating the answer inside the data, checkable from outside whoever
wrote the reference. The tolerance count matches ours exactly.

The datum count does not. The file says 6; there are 10 `DATUM` entities and our
reference says 10. Both are defensible: NIST counts datums established by datum
*features*, and assigns the four established by datum *targets* to the separate
`datum targets` line. **The disagreement is not an error on either side. It is
that "number of datums" names two quantities.** Five of the six solvers found the
discrepancy independently and three warned that a reference built on the file's
own figure would conflict with theirs.

An externally supplied check value therefore does not close the loop; it
relocates the question from *is this number right* to *what is this number
counting*, and the second question is not answerable by comparison. This is
worth stating because the design in §2 rests on external provenance — inputs,
procedure and reference all drawn from standards bodies and administrative
rulings — and it would be natural to read that as a solution to §3.1.1. It is
not. External provenance constrains the reference; it does not validate it.
Where the standard's terms are themselves ambiguous, provenance imports the
ambiguity along with the authority.

### 3.1.6 A task-statement defect the solvers could report, and a check that finds it

§3.1.5 reports a task-statement defect that **no solver could have reported**,
because the field's existence was never disclosed. A later task supplies the
complementary case: a task-statement defect of the same class that the solvers
**did** report, from a task that was under a pre-registered freeze at the time.

The counting task in the building-modelling benchmark (`bim`, T005) asks for
eleven figures over seventeen files, graded on exact match only. Two of the
eleven concern property rows. **The task statement did not fix whether
rows carried by non-physical owners were in scope.** Restricted to physical
elements the answers are 308 and 306; unrestricted they are 324 and 322. The
sixteen-row difference is ten rows on `IfcSpace`, three on `IfcBuilding` and
three on `IfcZone`. Both readings follow from the stated rules: the rules define
a property as an attribute inside a property set, and describe attachment as
being "to an element", a word the same rules use elsewhere in a narrower sense.

The submissions divide accordingly. Of the six runs, one produced no answers
(it exhausted its session limit); **the remaining five split two against three —
two wrote 308/306, three wrote 324/322 — and every run lost points at these two
questions and nowhere else.** A two-valued split with no scatter is the
signature of an interpretive fork rather than of arithmetic error. The run log
records that five runs additionally raised the ambiguity in prose.

Three things distinguish this instance from §3.1.5.

**The defect was recorded without being repaired.** The task statement,
reference, grader and adversarial suite had been frozen before the runs, in
response to an earlier task in the same benchmark whose reported effect turned
out to be an artefact of revising the grader after reading the submissions. The
freeze held: the defect is documented in the run log and the task is left
carrying it. The repair is a separate task with the two questions split into
four, frozen and not yet run. This is what §3.1.4's recommendation to publish
defect counts looks like when the defect is found in one's own current task.

**Solver-detectability of task-statement defects is not uniform.** In §3.1.5 the
answer format's worked example was structurally incapable of revealing that the
graded field existed, so the omission was unreportable and surfaced only as a
constant deduction under replication. Here both readings were derivable from the
material the solvers held, so the gap was visible to anyone performing the count,
and they reported it. The distinguishing property is not the solvers but the
statement: **whether it discloses enough for the gap to be apparent.** A defect
that suppresses a question is invisible to the subject; a defect that leaves a
question open is not. Only the second class is reachable by the detector of
§3.1.4, which narrows that section's claim.

**It yields a check that is not a function of the reference.** The three checks
of §3.1.1 cannot examine the task statement. This defect admits one that can:
recompute each figure under each admissible scope, and require that any question
whose answer moves names the scope **in its own text**. Applied to the task as
frozen, it fails on exactly the two property questions. Applied to the same
task's quantity question it passes, and passes for the informative reason — in
this corpus every quantity row is carried by a physical element, so the answer is
250 under either scope and the question is not exposed. The check's own
calibration is that it must fail on the frozen task; if it stops failing there,
the check has broken.

Its scope should not be overstated. It mechanises **one already-diagnosed class**
— the membership rule of a graded set — on one axis, and it was derived from a
solver report rather than reaching the defect first. It is not a general
procedure for finding disagreements between task and reference, and it does not
displace §3.1.4: the solvers found this defect, and the check was written
afterwards from what they found. What it demonstrates is narrower and still
worth stating: **once such a defect is diagnosed, the class it belongs to can be
made mechanically checkable, and the check runs outside the closed loop** because
its input is the task statement rather than the reference.

It repaid this immediately. Run against the draft of the repaired task, before
that task was frozen or issued, it failed two of the four replacement questions:
both had been written as continuations of the question above them ("as above,
but merged"), deferring scope to a neighbour. Submissions are maps from question
identifier to integer, so nothing obliges a solver to read the questions in
order. **The repair had reproduced the defect it was written to remove**, in a
form we had not noticed, and the check caught it before the task was issued.

### 3.1.7 The repair carried a second defect, and the check did not see it

The repaired task was frozen and issued to three runs of the code-executing arm.
All three returned every figure correctly. All three also reported, in the prose
accompanying their submissions and independently of one another, that **the task
statement printed the answers to four of its thirteen questions.**

They were right. The explanatory note we had written to document the defect of
§3.1.6 read, in part, *"restricted to physical elements 308/306, unrestricted
324/322"* — and those four numbers are the answers to the four questions the
repair had been built to ask. The nine remaining answers do not appear. **The
task could not measure the only thing it was made to measure.** We record it as
a failed measurement, leave the task unrepaired for the same reason as before,
and did not run the second arm, whose comparable cost on the preceding task was
of the order of five million tokens.

This is worth reporting for three reasons, none of them flattering.

**The defect was introduced by the repair, and the repair's own check did not
cover it.** §3.1.6 argues that a diagnosed class of task-statement defect can be
made mechanically checkable. That remains true, and it is now also clear how
little it buys: the check we wrote examines whether a question fixes the scope of
the set it grades, and answer disclosure is a different property of the same
artefact. Five checks ran on this task — calibration, external cross-check,
adversarial suite, the scope check, and a hash-based freeze — and the statement
carrying the answers passed all five. Adding a check for the class that just bit
us left us blind to the class that bit us next, in the same file, in text written
for the express purpose of explaining the first.

**The idea was already present and did not reach.** The benchmark's calibration
already contained a test for disclosed answers, written after an earlier task
leaked one; it inspects the worked example in the answer format. Counting tasks
have no worked example, so the test found nothing to examine and passed in
silence. The failure was not of conception but of coverage, and a check that
passes because it had nothing to look at is indistinguishable, in the log, from a
check that passed because the artefact was clean.

**The solvers found it again, and this time we had kept the evidence.** §3.1.4
recommends collecting and adjudicating solver reports as a matter of course. On
the preceding task we adjudicated them and then discarded them: the submissions
were stored as answer files only, and the ambiguity of §3.1.6 survives in a
curated run-log note rather than in the reports themselves. We changed that
before issuing this task, and the reports are what located this defect. Three of
three runs raised it unprompted, while returning correct answers — a solver
reporting that a question was too easy has no incentive we can identify, which is
the same structural point §3.1.4 makes about solver reports in general.

The wider claim of §3.1 is unchanged and, if anything, is made more sharply here
than by any instance we constructed deliberately. **A benchmark's checks are
written by whoever wrote the artefact they check, and inherit that person's
blind spots; the subject under test does not.** We have now watched this happen
three times in one benchmark: a defect the solvers could not see (§3.1.5), a
defect they could and did (§3.1.6), and a defect introduced by the act of
repairing the second, again found by the solvers and by nothing else.

### 3.1.8 The re-issue, and an examination-side defect that was the operator

The task was re-issued with the numbers removed from the explanatory note and
nothing else changed — questions, rules and input files are identical to the
character, which we verified mechanically. It was frozen and run three times on
each arm.

**The prediction held.** Both arms answered all thirteen questions correctly:
three of three runs on the code-executing arm, and two of three on the
read-only arm, with the third accounted for below. The two questions that three
of six runs had answered differently under the original statement were answered
identically by every run once the statement distinguished them. **No run
reported a disclosed answer**, against three of three on the previous issue.
The diagnosis of §3.1.6 — that the disagreement was a property of the question
and not of the solvers — is supported.

The remaining run is the finding. Partway through, the read-only arm's delegated
sub-agents began failing to return results through a secondary messaging channel,
and some of their output surfaced in the operator's stream instead of their
parent's. **We read this as a broken pipeline and instructed the two running
solvers to stop waiting and submit what they had.** One complied and returned
seven of thirteen, wrong by exactly one on all six questions that count spatial
entities and elements — the signature of a truncated pass. The other did not
comply, waited, and returned thirteen of thirteen; its final report states that
the channel had not been broken at all, only slow, that every outstanding result
arrived, the last about twenty-three minutes in, and that **had it followed our
instruction it would have scored zero on all thirteen.** It lists our
misdiagnosis explicitly among the examination-side defects it was asked to
report.

It was right, and the consequence is that **the operator became an
examination-side defect in the middle of a frozen measurement.** We were careful
in one respect and careless in another. Careful: we declined to relay the
delegates' output to their parent, on the grounds that someone holding the
reference should not carry messages inside the system under test, and we passed
no task content — only the instruction to stop waiting. Careless: that
instruction was itself an intervention, it was based on a misreading of a
transport failure as a pipeline failure, and it decided the difference between a
full score and a partial one on the run that obeyed it. The freeze held
throughout — the statement, reference and prompt template are byte-identical
before and after — and it did not help, because **a freeze constrains the
artefacts and says nothing about the operator's conduct during the run.**

Two further conditions of that arm were wrong and are worth stating because they
were wrong three issues running. The constraint text told the read-only arm it
could use three tools to search files; **two of the three do not exist in this
environment**, which we confirmed by probing a fresh session and reading the
error text, and the only working search route was the one the arm's own
constraint forbade. The arm was therefore reduced to reading seventeen files
linearly. The same defect is recorded against the first issue of this task, and
we nevertheless wrote in the run logs of the two subsequent issues that the
condition had been fixed. **We had not checked.** A false entry in the record is
worse than the original defect, because the original was visible to anyone who
read the log and the correction was not.

Consequently **the cost comparison for this task is void** — the read-only arm's
token counts mix the cost of its assigned handicap with the cost of a search
capability it was promised and did not have, and the two cannot be separated.
The attainment comparison is unaffected: reading linearly is slower, not less
correct, and the arm reached thirteen of thirteen twice.

A related gap: the prompt the solver actually received was a template with a
substitution slot, and **only the template was frozen.** The substituted text —
including the false claim about available tools — existed nowhere in the
repository until we transcribed it after the fact. A freeze that covers the
question but not the instructions is not covering what the solver read.

Finally, one observation about the limits of solver reports, which §3.1.4
recommends collecting. The truncated run declared its own least reliable figure
in its report. **That figure was correct, and its actual errors were in six
questions it had not flagged.** Solver reports have repeatedly located defects on
the examination side in this series; this one is evidence that they should not
be read as self-diagnosis. What the solver can see is the question it was asked.
What it cannot see is where its own count went wrong.

### 3.1.8 A defect no solver could report, found by external review

The instances above divide detection between two parties: the benchmark's own
checks, and the subject under test. A third case, which arrived after this
paper's first release and which we record here rather than omit, is located by
neither.

The building-modelling benchmark (`bim`) reported a task on which arm C scored
100.0 against arm B's 64.3 — a 35.7-point separation, and the only score
separation between those two arms anywhere in the series. In its v1.1.0 release
that benchmark withdrew the result, on the ground that the measurement had not
been sound. Three things had gone wrong, and they are of different kinds.

**A submission that read nothing scored full marks.** A submission constructed
without opening the corpus — entity identifiers enumerated across the four
positions the task asked about, with only the four differences set to the values
the task's own preamble implied — scored 100.0 out of 100. Every one of the six
real runs scored between 55.0 and 70.0. **The observed scores were all below
what an uninformed submission obtained**, which is the signature of a grader
that is not measuring the quantity it names: one question was scored on coverage
alone, so enumerating widely drove recall to 1.0, and the other required only
four differences to be stated.

This is the mechanism of §3.1.1 carried one step further than we had stated it.
We had said the adversarial suite is blind in the direction where the reference
is wrong, because its cases are built by corrupting the reference. The stronger
consequence is that the suite is untested *everywhere far from the reference*:
a perturbation-generated suite cannot reach a submission that bears no relation
to the reference at all. The suite passed — nine cases at the time — and had
never probed the region in which the grader was degenerate. The repair was to
add uninformed submissions as standing adversarial cases, at which the same
submission scores 1.6 while the reference still scores 100.0.

**The solvers could not have reported it.** This is the respect in which the
case differs from §3.1.5, where the solvers were silent about a defect they
were in a position to notice. Here the defect concerns what the grader does
with submissions that no solver produces. A solver that reads the corpus and
answers honestly never visits that region of the submission space, and so has
no observation to make about it. Neither routing through solver reports (§6)
nor comparing per-question breakdowns across repeated runs reaches this class:
the six runs *did* share a deduction, but the shared deduction was the
symptom of a low ceiling, not of the degeneracy above it.

**The stated reason for the withdrawal was itself wrong, and the error was
recoverable only from version control.** The withdrawal was first attributed to
replication — that the separation seen in a pilot run had not survived n = 3.
Restoring the pre-revision grader from version control and re-scoring the pilot
submissions gave a different account:

| | grader as frozen | grader after revision | change |
|---|---|---|---|
| pilot arm B | 11.7 | 64.3 | **+52.6** |
| pilot arm C | 71.7 | 100.0 | +28.3 |

The revision moved more points than the 35.7-point separation being withdrawn.
The revised task statement had also resolved, in its rules, the single fact arm
B had failed on. The pilot and the replication were therefore not runs of the
same task, and the correct account is not that the separation vanished under
replication but that **the statement and the grader were revised after the
submissions had been read**. We note that this is available as a check only
because the grader is under version control and every revision is a commit;
a benchmark distributed as a snapshot cannot be interrogated this way, by its
authors or by anyone else.

A replacement task, with the task statement, reference, grader and adversarial
suite committed before any arm was run and untouched afterwards, was measured at
n = 3 per arm. Both arms reached 11 of 11 — the separation did not reappear —
and the arms differed on cost alone (arm B 370,646–447,227 tokens, arm C
89,683–115,518). The one examination-side defect that survived into that task
was reported by five of the six runs, independently, and was left in place
rather than repaired mid-measurement.

Two consequences follow for the argument of §3.1. First, the detector inventory
is three, not two: the checks, the subject under test, and review of the
*method* by a party who did not write it. The third is the only one of the three
that can examine the grader's behaviour on inputs the design never generates.
Second, the freeze is not a formality. The discipline that made this case
diagnosable at all — every artefact committed, every revision dated — is the
same discipline that would have prevented it.

---

## 3.2 How far three known effects vary across domains

The three effects below are documented in prior work. What the series adds is
their magnitude when the domain is varied and the design is held fixed. We are
not claiming the phenomena.

### 3.2.1 Supplying the governing material — reported range and sign

That retrieval or augmentation helps unevenly, and can hurt, is established in
the retrieval literature: augmentation improves recall broadly while degrading
ranking metrics for some task categories, benefits saturate with scale, and the
strongest configurations can degrade under every rewriting technique examined.

Measured across these domains, the spread is wide enough to change sign:

| Domain | Material supplied | Effect |
|---|---|---|
| Civil CAD (`doboku`) | A written description of the SXF format | **25 → 97 / 100** |
| Quantity takeoff (`sekisan`) | Relevant articles of the surveying standard | Largest single factor |
| Customs classification (`kanzei`) | Tariff schedule, notes, precedents | **Arm B below arm A** |

In `doboku`, arm A could not emit a readable file at all and is disqualified at
25/100; a description of the file format — nothing about the drawing — lifts
arm B to 97/100. In `kanzei`, enlarging the material from 0.81 to 4.4 million
characters **changed none of the 61 answers**: four were corrected and four were
broken. Decomposed, 34 of 61 (56%) are answered correctly under every
condition, 15 remain wrong under all of them, and 12 move. Every case that broke
cites the correct provision and then reaches the wrong conclusion — the material
was read and did not govern.

### 3.2.2 Cost at the point where scores tie

Reporting efficiency alongside accuracy is not new; HELM treats efficiency as
one of seven metrics measured for every scenario, and cost-per-task now appears
as a default column on public leaderboards. The observation here concerns what
happens **after scores have saturated**.

**A replicated measurement.** `jiban` T002 was subsequently re-run three times
for each of arms B and C, under the isolation conditions of §2.4 and with
subagent spawning explicitly prohibited, so that the confound in §4.2.3 does not
apply. **All six runs scored 100 out of 100.** Reported liquefaction potential
indices agreed across all six to within 0.002 percent — arm C reproduced itself
to within 4e-6, arm B, computing by hand, drifted by up to 2.6e-4.

| | tokens (3 runs) | mean | SD | CV | tool calls |
|---|---|---|---|---|---|
| arm B (no execution) | 230,707 / 225,229 / 243,547 | **233,161** | 9,402 | 4.0% | 15.7 |
| arm C (execution permitted) | 115,948 / 104,220 / 111,282 | **110,483** | 5,905 | 5.3% | 26.0 |

**The separation is 2.11x, and the difference of 122,678 tokens is 15.6 times
the pooled standard deviation.** Run-to-run variation in consumption is real —
4 to 5 percent — and it is nowhere near large enough to account for the gap.
This supersedes an earlier version of this paper, which reported that we could
not determine whether the difference exceeded variance (§4.4).

Note the direction of the tool-call count: **arm B made fewer tool calls and
consumed more than twice the tokens.** Prohibited from executing code, it
carried the arithmetic in context instead. What execution purchases here is the
replacement of in-context computation with delegated computation, and the
purchase is favourable by a factor of two.

The trend across task size, measured earlier at n = 1, is consistent with this:
enlarging the task 8.7-fold in assessable points grew arm B's token use 3.3x and
arm C's 1.8x, so the unit-cost gap widened from 1.37x to 2.6x. That
trend rests on single runs and is reported as corroboration, not as
measurement.

**A second domain, replicated to the same protocol.** `kikai` T001 was re-run
three times per arm under the isolation and no-subagent rules above. It differs
from `jiban` in that the task is extraction rather than computation: the answer
is read out of a STEP AP242 file, not derived from it.

| | mean tokens | SD | mean seconds | mean tool calls | score |
|---|---|---|---|---|---|
| arm B (one-shot) | 126,286 | 2,837 (2.2%) | 258 | 13.3 | 94.6 |
| arm C (execution permitted) | **84,614** | 3,151 (3.7%) | **402** | **25.3** | 94.6 |

The separation is 1.49x at **13.9 pooled standard deviations**, with no overlap
between the arms' ranges (arm B 123,070–128,436; arm C 81,122–87,246). The sign
agrees with `jiban`: permitting execution reduces token consumption where the
alternative is holding the input in context.

**But the same measurement reverses on a different resource.** Arm C took 1.56x
the wall-clock time and 1.9x the tool calls to reach the identical answer. It
writes a parser, runs it, finds it wrong, and fixes it — the three arm C runs
each reported a different self-caught error, all in the STEP parsing itself —
whereas arm B reads the file and answers. Execution trades tokens for round
trips. **Which arm is "cheaper" is therefore not a property of the arms; it is
determined by which resource the question is about,** and every cost figure in
this section is tokens.

The scores are equal to the decimal place — 94.6 in all six runs, with the same
per-question breakdown — so this is again a case where a benchmark reporting
only score would record the two configurations as equivalent. The 5.4 points
lost in common are an examination-side defect of ours, analysed in §3.1.5.

One further observation is consistent and is reported as such: in `bim`, arm C
scored 255/255 against 235/255 while consuming 98,901 tokens against 371,572.
That is not a controlled measurement of cost.

A benchmark reporting only score would record the `jiban` configurations as
equivalent at both task sizes.

**A replicated measurement, and what the extra cost buys.** In `cad`, task T004
was run five times for each of arms A, B and C. The *scores* are therefore a
distribution rather than a point. The *costs* are not: they were retained only
as per-arm means over the five runs, so the figures below are averages and no
spread is available for them (§4.4).

| | mean tokens / run | mean tool calls / run | median score | worst score |
|---|---|---|---|---|
| arm B (one-shot) | 107,929 | 9.2 | 99.6% | 91.1% |
| arm C (execution permitted) | 184,379 | 57.6 | **100.0%** | **97.2%** |

Here the sign is opposite to `jiban`: **arm C is the more expensive
configuration**, at 1.7 times the tokens and 6.3 times the tool calls. What that
buys is 0.4 points of median accuracy — and 6.1 points of *worst case*.

This is the more useful way to read it. The median difference is negligible and
would be discarded as noise. The tail difference is not: arm B's worst run
scored 91.1%, and the failure mode behind such runs is a dimension rendered at a
hundred times its true value. **The expenditure purchases the absence of that
run, not a better typical run.** §3.2.3 shows that the same distinction —
between what happens typically and what happens on repetition — is where the
domains separate most sharply.

Taken with `jiban`, the two replicated or trended observations do not point the
same way, and we do not combine them. In `jiban`, at exactly tied scores, the
configuration permitted to execute code was the cheaper one and its advantage
grew with task size. In `cad`, at nearly tied medians, the configuration
permitted to execute code was the more expensive one and its advantage was
concentrated in the tail. **What execution buys is not fixed across domains**;
in one it reduced unit cost, in the other it bought tail reliability at a
premium.

### 3.2.3 Non-determinism, and a pattern success rates cannot express

Reliability under repetition is an established axis. τ-bench introduced `pass^k`
— the probability that all of k repeated runs succeed — and reported the gap it
exposes (61% at pass@1 against 25% at pass@8 for one system), and subsequent
work has built on it.

Across domains, holding conditions identical:

| Domain | Answer type | Runs | Cases whose answer changes |
|---|---|---|---|
| Quantity takeoff (`sekisan`) | quantities | 5 | **0%** — task S005 identical to the character |
| Geotechnical assessment (`jiban`) | vector of reals | 3 | **0%** at the grader's tolerance; **100%** at exact match |
| Tolerancing (`kikai`) | discrete extraction | 6 | **0%** — all 28 items identical every time |
| Customs classification (`kanzei`) | one discrete code | 5 | **25%** — 46/61 identical every time |
| Tax provision retrieval (`zeimu`) | set of provisions | 5 | **82%** — 14/78 identical every time |

**The `jiban` row is not commensurable with the others, and neither, on
inspection, are the rest.** Where the answer is a discrete code (`kanzei`), a
set of identifiers (`zeimu`), or a list of entities extracted from a file
(`kikai`), "the same answer" is well defined and exact comparison is the natural
test. Where the answer is a vector of real numbers
(`jiban`), exact comparison is not a meaningful test: none of the six `jiban`
runs reproduced another to the last digit, while all eight cases agreed within
the grader's tolerance of one percent. Measured at four significant figures, the
arm permitted to execute code agreed with itself on all eight cases and the arm
computing by hand agreed on none.

So the figure for a real-valued domain is a function of the tolerance, and the
0-to-82-percent spread reported here mixes two kinds of measurement. `sekisan`
is the one real-valued case that is exactly reproducible — its output was
byte-identical across five runs — which suggests the distinction is not purely
an artefact of the metric: a task whose rule fully determines a rounded output
can be exactly stable, while one requiring an unrounded chain of computation is
stable only to a stated precision. **A cross-domain reliability figure needs to
state its tolerance, and the literature convention of a binary success criterion
hides that it is doing so.**

Restricting attention to the three domains where exact comparison is meaningful
does not narrow the spread: it runs from 0% to 82%. `kikai` sits at the stable
end. Its task extracts every geometric tolerance from a STEP AP242 file — 28
items with their types, values, datum references in priority order, and material
modifiers — and across six runs (two arms, three each) every one of the 28 was
reproduced identically, down to the ordering of datums within each frame. The
graded score was 94.6 in all six, and the per-question breakdown was identical
as well. **Discreteness of the answer is therefore not what makes a domain
unstable.** `kikai` and `kanzei` both have discrete answers and sit at opposite
ends. What separates them is that `kikai` asks what a file contains, while
`kanzei` asks which of several defensible categories a described good belongs
to; the first has a determinate answer to read off, the second requires a
judgement that the system does not make the same way twice.

`kanzei` scored 41, 42, 39, 41, 42 (range 3, SD 1.10) across the five runs. The
score is stable to about a point; the answers are not. Decomposed by behaviour
across runs, 35 cases are right every time, 11 wrong every time, and 15 depend
on the draw — a split that closely matches the 34 / 15 / 12 obtained by varying
the *material* instead of the *run*. Two different cuts of the same data give
the same shape.

**The `zeimu` result is the one `pass^k` cannot express.** Because the answer is
a *set* of statutory provisions rather than a single outcome, success is not
binary and the run-to-run difference can be decomposed. Over five runs of 78
cases, correct-citation counts were 81, 82, 75, 82, 78 and submitted-citation
counts were 151, 153, 150, 143, 148. Within the 64 unstable cases:

> **In 32 of them — exactly half — the number of correct citations is identical
> across all five runs while the set itself is not.**

The system exchanges one correct provision for another, or one incorrect
provision for another, and the score does not move. A success-rate metric,
`pass^k` included, collapses each case to succeeded-or-not and cannot represent
a case that scores identically five times by five different routes. Where the
requirement is that the same question receive the same answer — tax opinion,
audit, regulatory filing — this is the failure mode of interest, and it is
invisible to the metrics currently used to report reliability.

---

## 3.3 Two observations from the geotechnical benchmark

Both observations below come from `jiban` alone. We report them because they
bear on how the arms fail rather than on how much they score, and we have not
attempted to confirm them in the other seven domains; they should not be read
as properties of the series.


**Missing data is reported as missing.** In `jiban`, all four arms independently
flagged that condition 3 of the assessment criteria (D50 ≤ 10 mm and D10 ≤ 1 mm)
could not be verified for a gravelly layer, stated that they had nonetheless
included it in scope, and two read the field description far enough to offer a
conditional second answer for the case where it is excluded. Refusal to assert
beyond the data did not discriminate between arms.

**The failures that matter are recall, not arithmetic.** Where arm A lost points
in `jiban`, it lost them by retrieving the superseded 2012 formulation of the
cyclic strength ratio. It scored full marks on scope selection and on stress
computation — the parts requiring the data to be read correctly — and failed on
the part requiring knowledge of which edition of the standard is in force. This
is the same error the author made before consulting the primary source, and it
is the error the adversarial suite was built to catch (§2.2).
