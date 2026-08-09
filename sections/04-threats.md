# 4. Threats to validity

Several of the limitations below were discovered only after results had been
produced, and some were found by the subjects. Where a limitation invalidates a
claim made in an earlier version of this work, that is stated.

---

## 4.1 Construct validity

### 4.1.1 We identify the reference-solution problem; we do not solve it

Section 3.1 argues that no check defined in terms of the reference solution can
detect an error in it, and reports that fourteen of fifteen examination-side
defects were located by the solvers instead. **That is a diagnosis, not a
remedy.** It leaves this work in the position it describes.

Specifically, we know how many defects were *found*. We do not know how many
exist. The detector that worked — a solver with the raw inputs and no answer key
— is opportunistic: it reports a defect when it happens to notice one and
happens to say so, and its coverage is neither controlled nor measurable. A
domain whose solvers reported nothing is not thereby shown to be clean; it may
only be a domain where the defects lie outside what a solver would notice.

Nothing in this paper establishes a bound on residual defects in any of the
eight reference solutions, and the results in §3.2 rest on those references.
Every number in §3.2 should be read as conditional on reference solutions of
unknown remaining error.

### 4.1.2 Task difficulty was calibrated after the fact

In `jiban`, arms B, C and D all scored 100/100 on the first task and still all
scored 100/100 when the task was enlarged roughly sixfold in assessable points.
The benchmark was measuring a single axis — whether reference material is
supplied — and not the axes it was designed to separate. This was addressed by
reporting cost rather than score (§3.2.2), which is a change of instrument, not
a fix to the task. **Difficulty should be verified by running the arms before
the task is built out.**

### 4.1.3 The rubric is authored by the same person as the task

Each grader was written by the author. The adversarial suite (§2.2) requires it
to reject deliberately broken submissions, including the case that motivated the
design — a solution computed with the superseded 2012 formulation, numerically
plausible and accepted by a permissive grader. This establishes that the grader
is not trivially fooled. It does not establish that the rubric weights the right
things, and by §3.1.1 it cannot.

---

## 4.2 Internal validity

### 4.2.1 Most results are n = 1, and the one n = 5 overturned a published reading

Every benchmark except `kanzei` and `zeimu` was run once per arm. Repeating
`kanzei` five times under identical conditions gave:

```
run1 41/61     run2 42/61     run3 39/61     run4 41/61     run5 42/61
range 3        SD 1.10        total score 80.5 – 84.9
```

A score of 42 had been observed three times across three earlier rounds and read
as a stable ceiling. It is the **top of the range**, drawn three times. The
earlier reading that the arm with a validator performs worse — arm C at 42
against arm D at 39 — does not survive: **that difference lies entirely within
arm C's own variance.** It was an artefact of n = 1.

A second domain shows the same failure more severely. In `cad`, task T004 was
run five times for each of three arms:

```
              arm A        arm B        arm C
worst          0.0%        91.1%        97.2%
median        94.2%        99.6%       100.0%
mean          77.7%        97.5%        99.4%
```

The single-run ordering had been arm A (100.0) > arm C (97.2) > arm B (94.4).
**All three single runs were unrepresentative**: arm A's drew the maximum of its
distribution, arm B's near its minimum, arm C's its minimum. At n = 5 the
ordering is arm C > arm B > arm A on median, mean and worst case alike — the
**reverse** of what one run reported. The section of that benchmark's write-up
which had concluded that the weakest-equipped arm performed best was withdrawn.

Single-run comparisons in this work carry an implied uncertainty of at least
±1.5 points; differences below about 3 points should not be interpreted. The
`cad` result suggests this is too generous where the distribution is skewed:
arm A's range there spans 100 points, and no bound derived from a symmetric
assumption applies to it.

### 4.2.2 The n = 5 replication was not isolated

The five working directories were placed under a shared scratchpad. A previous
arm's `build_answers.py` — holding all 61 case identifiers and 49 of the
nine-digit codes — was reachable from each run. Run 2's report states that it
found and discarded a previous run's `t.py`, confirming that at least one run
looked outside its working directory.

Agreement with the previous arm C ranged from 87 to 95 percent and no run
reached 100, so there is no evidence of copying. But **contamination acts toward
agreement**, so the 25 percent disagreement in §3.2.3 is a **lower bound**.
Isolation rules were written into the protocol only after this was found.

### 4.2.3 Arms spawned subagents at differing widths

During the replication the arms launched parallel subagents: four in run 3, six
in run 4, five in run 5. This was not prohibited and is not a protocol
violation, but the observed variance carries a component from the arm's internal
parallelism, which was neither controlled nor recorded. Later protocols state
explicitly whether subagents are permitted.

### 4.2.4 The validator arm did not hold its tooling constant

In `kanzei`, arm D ran three times and **its validator differed on all three
occasions** — one round had a broken chapter-note correspondence table, another
had three defects that arm D itself reported. The three results are not three
samples of one condition, and the single round in which arm D outscored arm C
cannot be attributed to the validator.

### 4.2.5 Arm configuration is not uniform

| Arms present | Benchmarks |
|---|---|
| A, B, C | `cad`, `sekisan`, `doboku`, `zeimu` |
| A, B, C, D | `kanzei`, `jiban` |
| B, C | `kikai`, `bim` |

**The arms are also not defined on the same axis in every domain.** §2.4
presents A, B, C and D as differing in reference material, code execution and
validation. That holds for `sekisan`, `doboku`, `jiban`, `kanzei` and `zeimu`,
where arm A is distinguished from arm B by whether the governing material is
supplied. It does **not** hold for `cad`, where arm A is distinguished from arm
B by whether a drawing library may be used at all — arm A writes the file
format directly, arm B is permitted a library — so the `cad` A-versus-B contrast
measures tooling rather than material. `cad` is accordingly excluded from
§3.2.1, but this was originally a consequence of which comparisons were
available rather than a deliberate exclusion, and the discrepancy in the arm
definitions was noticed only during preparation of this paper.

The B-versus-C contrast is consistent across domains — in every benchmark it is
the addition of code execution — so the cost observations in §3.2.2 are not
affected.

Only B and C appear in all eight domains, so **every cross-domain claim in §3.2
is restricted to B and C**. Statements involving arm A rest on six domains and
those involving arm D on two. In particular, the sign reversal in §3.2.1 is an
A-versus-B comparison available in `doboku` and `kanzei` but not in `kikai` or
`bim`.

---

## 4.3 External validity

### 4.3.1 The arms are scaffolding variants, not different models

A, B, C and D differ in the material and tooling supplied, not in the underlying
model. Nothing here compares model families, and no result should be read as a
ranking of models. The cost finding in §3.2.2 is a statement about scaffolding,
measured on one model.

### 4.3.2 One operator designed, built, graded and ran everything

Task design, reference implementation, grader, adversarial suite and execution
were carried out by the author. There is no independent replication of any
result. This is the reason for the release in §7, and it is a particularly sharp
limitation given §4.1.1: the person who wrote the reference solutions is the
person reporting how many defects they contained.

### 4.3.3 Domain coverage is Japan-specific and chosen by one person

Seven of eight domains are governed by Japanese national standards, file formats
or administrative rulings. This is deliberate — it is why the benchmarks exist,
these domains being absent from existing work — but it limits generalisation.
Whether the sign reversal in §3.2.1 tracks *format-constrained versus
judgement-constrained* tasks, as we suggest, or something particular to these
standards, cannot be settled from eight domains chosen by one person.

### 4.3.4 Task difficulty is not matched across domains

Nothing equalises difficulty between the eight benchmarks. Each task was built
to what the domain's standard demanded, not to a common target, so a
cross-domain difference in effect size is confounded with a cross-domain
difference in how hard the tasks are and how much the arms were given. The
sign reversal in §3.2.1 admits an alternative reading on exactly these grounds:
arm A in `doboku` may have failed because the format is unfamiliar, or because
the specification it received was thinner than what arm A received in `kanzei`.
We cannot separate these, and the design does not permit it.

### 4.3.5 Two domains have substantially larger prior work

`kanzei` addresses a task for which prior work reports fine-tuning on 18,731
customs rulings and a 632-entry expert-annotated benchmark; `bim` addresses one
for which prior work provides 324 tasks over 11 building models. Against those,
four and two tasks are small. Their contribution here is participation in a
cross-domain comparison under one design, not classification accuracy.

---

## 4.4 What is not resolved

- **Token variance between runs was never measured, in any domain.** This
  correction supersedes an earlier statement in this section. `cad` T004 was run
  five times per arm and the per-run *scores* were retained, but the token
  counts were recorded only as per-arm means; the individual runs' consumption
  was not kept. `jiban` reports a trend across two task sizes from single runs.
  **No domain in this series supplies a distribution of token consumption**, so
  the widening from 1.37 to 2.6 in §3.2.2 cannot be compared against run-to-run
  variance. The tie at 100/100 at both sizes constrains the interpretation, in
  that no accuracy difference can be trading against cost, but it does not bound
  the variance.

  The gap was found while auditing the repositories after this section was
  first written, which is the same failure mode as §3.1: a claim about our own
  measurements that our own records did not support. §3.2.2 reports a trend
  across two task sizes, but both points are single runs. We know score varies
  between runs (§4.2.1) and we know at least one source of token variance
  operated during this series — arms spawning four, six and five subagents on
  three runs of one task (§4.2.3) — but we have no estimate of the resulting
  spread in consumption. **We therefore cannot say whether the widening from
  1.37 to 2.6 exceeds run-to-run variance.** The tie at 100/100 at both sizes
  constrains the interpretation, in that no accuracy difference can be trading
  against cost, but it does not bound the variance.
- **Cost is instrumented in four domains, at two different granularities, and
  claimed for two.** §3.2.2 draws
  its claims from `jiban` (trend across task size, n = 1 at each point) and `cad`
  (n = 5 for score, per-arm means only for cost, one task); `kikai` and `bim` are reported as
  consistent observations, and the `kikai` figure is contaminated by a defect of
  ours (§3.1.3). The instrumentation exists in all eight; the runs have not been
  redone.
- **Repetition exists in two domains.** §3.2.3 rests on `kanzei` and `zeimu`.
  The claim that non-determinism is domain-dependent would be considerably
  stronger with a third and fourth measurement, and the `sekisan` 0 percent
  figure comes from a single task rather than a full replication.
- **`zeimu`'s replication is not written up in its own repository.** The five
  runs exist as data; the analysis in §3.2.3 was computed for this paper. An
  earlier informal reading of those runs, quoting 74 percent disagreement and a
  citation hit count stable to ±1, does not survive recomputation with the
  benchmark's own normaliser: the values are 82 percent and a spread of 7.
  **The figures in §3.2.3 supersede it.**
- **The defect count is a floor, not an estimate** (§4.1.1). Fifteen were found
  in `kanzei` and four in `jiban`. Nothing here bounds what remains, in those
  two domains or in the six where no defect has yet been reported.
