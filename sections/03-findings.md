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

One defect was an operator error and is recorded because the failure mode
generalises. The tariff data was maintained as two artefacts — a structured
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

**In this design the subject under test was the only detector that located
reference defects at all.** With fifteen instances we cannot rank detectors —
the defects a solver finds are, by construction, the ones a solver can find,
and the single defect our own checks caught may belong to a class they are
good at. The claim is about what worked here, not about relative power.

We know of no procedure internal to the benchmark that substitutes for it, and
we did not find one.

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

**Scope of this claim.** Cost was recorded from single runs, and we show
elsewhere that single runs are unreliable in this series (§4.2.1). Token
consumption is if anything less stable than score: §4.2.3 reports that arms
spawned four, six and five subagents on three runs of one task, which alone
moves consumption substantially. **We therefore make the claim only for
`jiban`**, where the scores are *exactly* equal so that no accuracy difference
can be trading against cost, and where the effect is visible as a *trend across
task size* rather than as a single ratio. The other two domains are reported as
consistent observations, not as measurements.

In `jiban`, arms B, C and D all reached 100/100 on both tasks. Enlarging the
task 8.7-fold in assessable points grew arm B's token use 3.3x and arm C's 1.8x
— both sublinear, at different rates — so the unit cost separated as the task
grew:

```
T001 (6 points)     arm C  ~1,245 tok/point     arm B  ~1,705 tok/point     gap 1.37x
T002 (52 points)    arm C   1,705 tok/point     arm B   4,392 tok/point     gap 2.6x
```

The trend is the claim: **at identical scores, the cheaper configuration
remained cheaper and the gap widened with task size.** A single-run ratio would
not support this; two points on a size axis, both at tied scores, do.

Two further observations are consistent with it and are reported as such. In
`kikai`, arm C covered 6 of 6 files against arm B's 5 of 6 while consuming
216,591 tokens against 1,053,066 — though arm B's figure includes 551,489
tokens spent by subagents pursuing a phantom reference caused by a defect in
our own parser, so the comparison is contaminated by §3.1.3. In `bim`, arm C
scored 255/255 against 235/255 while consuming 98,901 tokens against 371,572.
Neither is a controlled measurement of cost.

A benchmark reporting only score would record the `jiban` configurations as
equivalent at both task sizes.

**A replicated measurement, and what the extra cost buys.** One domain does
carry cost at n = 5. In `cad`, task T004 was run five times for each of arms A,
B and C, so the distribution is available rather than a point:

| | tokens / run | tool calls / run | median | worst |
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

| Domain | Runs | Cases whose answer changes |
|---|---|---|
| Quantity takeoff (`sekisan`) | 5 | **0%** — task S005 identical to the character |
| Customs classification (`kanzei`) | 5 | **25%** — 46/61 identical every time |
| Tax provision retrieval (`zeimu`) | 5 | **82%** — 14/78 identical every time |

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
