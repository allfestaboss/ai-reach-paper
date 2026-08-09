# 6. Discussion

## 6.1 Why the material effect might reverse sign

*The reading offered here is post hoc. It was arrived at by inspecting results
already obtained, was not predicted in advance, and is presented as a hypothesis
to be tested rather than as a finding.*

Section 3.2.1 reports that supplying the governing material moves one task from
25 to 97 out of 100 and leaves another entirely unmoved under a 5.4-fold
increase. A reading consistent with all eight domains, though not established by
them, distinguishes what the material contains.

In `doboku` the material is a **description of a file format**. The system could
not emit a readable SXF file without it, and could with it. What was supplied
was a generative grammar the system lacked: given the grammar, the output is
largely determined. In `sekisan` the material is a set of **deduction rules** —
openings below 0.5 m² are not deducted, quantities are carried to one decimal
below 100 and to integers above — and those rules *are* the answer; a system
that has them can compute, and a system without them cannot guess them.

In `kanzei` the material is a **tariff schedule with explanatory notes**. The
system already possessed the structure of the schedule; what it lacked was the
judgement of which heading a described consignment falls under. Supplying more
of the schedule supplies more of what it had. This is visible in the failure
mode: every case that broke under the enlarged material cites the correct
provision and reaches the wrong conclusion. The material was read and did not
decide.

The distinction is between material that **determines** the output and material
that **contextualises** a judgement. Where the missing thing is a formalism, the
effect is large; where the missing thing is judgement, additional material is
near-inert and can displace attention from what the system already had.

This predicts something testable: in a domain where the system lacks the
formalism — an unfamiliar file format, an unfamiliar calculation procedure —
supplying it should produce a large gain, and in a domain where the formalism is
already known, it should not. §2.5 groups the eight domains into generation,
extraction, and classification or identification, which is a first approximation
to this split, but three domains cannot separate the two explanations and we do
not claim it is settled.

## 6.2 Building the solver into the audit

If the detector that located reference defects is a solver holding the inputs
and not the answer key (§3.1.4), that role can be arranged deliberately rather
than relied upon as a by-product. Three changes follow, all cheap.

**Run a solver before the reference is fixed.** The defects in §3.1.3 were found
after scores had been computed, which meant discarding a round of results. A
solver run against a provisional reference, with its report read before any
score is published, converts the same detector into a pre-release check.

**Give one solver an explicit adversarial brief.** In this series the reports
arrived unbidden, as remarks appended to submissions. A solver asked directly to
identify inconsistencies between the task statement, the inputs and the standard
— and scored on nothing — is doing the same work under instruction. It has the
property that matters: it reasons from the instance's inputs and cannot see the
answer key.

**Adjudicate the reports rather than discarding them.** Of the fifteen
examination-side defect reports in `kanzei`, fourteen were correct. A reviewer
disposed to read such remarks as excuses would have discarded fourteen true
defect reports to avoid one false one.

None of this closes the gap identified in §4.1.1. A solver notices what a solver
notices; coverage remains uncontrolled and unmeasured. The claim is only that
the detector which demonstrably worked can be operated on purpose.

## 6.3 Defect counts should be reported

We suggest that a benchmark publication state how many defects were found in its
own tasks, reference solutions and supporting material; by what route each was
found; and whether the reported results predate or postdate the corrections.

The argument is that the absence of such a statement is uninformative in a
specific way. A benchmark that reports no reference defects may have none, or
may not have looked, or may have looked and not said — and a reader cannot
distinguish these. Publishing the count makes zero meaningful. It also makes the
count comparable: the figures in §3.1.3 are unremarkable on their own, but they
are the only figures of their kind we are able to cite, including our own.

We have applied this to ourselves before proposing it: §3.1.3 and §7.3 report
our own counts, including a defect that was our own operator error and that
reached the answers. The proposal is not that others do something we have not.

There is an obvious objection, which is that reporting defects invites the
inference that the benchmark is unreliable. We think the inference runs the
other way, and note that the same argument was resolved in this direction for
label errors after Northcutt et al. and MMLU-Redux: the benchmarks whose error
rates are known are the ones that can be used carefully.

## 6.4 External authorship is necessary and not sufficient

Section 2.1 requires that inputs, procedure and reference all come from outside.
At the strongest degree the designer contributes no content: the reference is a
function of two external artefacts. §3.1.2 is a defect in exactly such a
reference.

External authorship removes the designer's judgement from the **content** of the
answer. It does not remove the designer's judgement from the **implementation**
of the derivation, and that is where the defect lived — a choice about
integration bounds that the standard does not state in a form the code can
inherit. The strongest remaining check we can identify is **independent
reimplementation**: a second derivation of the same reference, by a different
person, from the same external sources. That is expensive, and we have not done
it. Releasing the reference implementations (§7) is the cheapest available
approximation, in that it makes reimplementation possible for anyone who cares
to.

## 6.5 A note on what saturation means here

One domain produced an exact tie at full marks across both its tasks, and
enlarging the second 8.7-fold did not break it (§3.2.2). The usual reading is
that the task is too easy and should be retired or made harder.

We suggest a second reading. A tie at full marks whose cost gap widens from
1.37 to 2.6 times as the task grows is not an absence of signal; it is a signal
on a different axis, and retiring the task discards it. The domains where accuracy has saturated are
precisely the domains where the practical question has moved from *can it be
done* to *at what cost*, which is the question a practitioner deciding whether
to adopt the system is actually asking.
