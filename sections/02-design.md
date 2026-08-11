# 2. Design

The eight benchmarks share four constraints. They are stated here as
requirements because each was adopted after a failure that it prevents; §3.1 and
§4 report where they nonetheless proved insufficient.

---

## 2.1 Nothing in the ground truth is authored by us

A reference solution written by the task designer cannot be checked by the task
designer. Every check available to them — recomputation, adversarial testing,
inspection — runs through the same understanding that produced the reference.
The requirement is therefore not that the reference be *carefully* authored but
that it be **externally** authored.

External authorship is achievable in three degrees, and the series moved through
them in order.

| Degree | What comes from outside | Example |
|---|---|---|
| 1 | The **answer** | `kanzei` — Japan Customs' published advance rulings supply the tariff code for each described consignment |
| 2 | The answer **and the procedure** | `sekisan`, `doboku` — a national surveying standard and a published file-format specification determine how the answer must be derived |
| 3 | The answer, the procedure **and the input** | `jiban` — measured borehole logs from state-commissioned surveys, a national bridge design standard, and a reference solution obtained by running the second mechanically over the first |

At degree 3 the designer contributes no content at all: the reference solution
is a function of two external artefacts, and the designer's role reduces to
implementing that function. This does not make the implementation correct —
§3.1.2 is precisely a defect in such an implementation — but it removes the
designer's judgement from the answer.

Degree 1 leaves the most exposure. Where only the answer is external, the
designer still decides what the question is, and can unknowingly pose a question
the authority did not answer.

## 2.2 The grader is validated before it is used

No score is reported until the grader has been shown to reject deliberately
corrupted submissions. Each benchmark carries a suite that generates such
submissions from the reference solution: shifting depths, scaling a result by a
power of ten, inverting a binary judgement, omitting cases, swapping labels
between conditions, submitting an empty or whitespace answer. A benign case —
the reference rounded to four significant figures — must still pass, so that the
suite tests discrimination rather than strictness.

The case that motivated the requirement is worth stating, because it is the one
a permissive grader accepts. Japan's bridge design standard revised its
liquefaction strength formulation in 2017; the superseded 2012 formulation
differs in the correction for fines content and in the low-density branch of the
cyclic strength ratio. A submission computed with the 2012 formulation produces
values of the right order and the right shape. It is wrong, and a grader with
loose tolerances scores it full marks.

The suite is run first. If any case fails — if the grader accepts a submission
it should reject — no arm results are computed for that task.

**This validates the grader against the reference. It does not validate the
reference** (§3.1.1).

## 2.3 Quantities that cannot be derived are supplied as givens

Where the standard requires a value the input data does not contain, that value
is stated in the task rather than chosen by the reference implementation. In
`jiban` this covers the unit weight of soil, the design groundwater level and
the seismic coefficient. Each is a real decision made by a practitioner —
groundwater level in one hole was measured four times at 3.40, 1.46, 4.13 and
3.41 m, and selecting a design value from those is a judgement — and each would
otherwise reintroduce the designer's discretion into the reference solution,
defeating §2.1.

The boundary is drawn at derivability: if the standard plus the supplied data
determine the value, the reference computes it; if not, the task states it.

## 2.4 Arms are not bundled

Four configurations are distinguished. They differ in what is supplied, not in
the underlying model.

| Arm | Reference material | Code execution | Independent validator |
|---|---|---|---|
| **A** | — | — | — |
| **B** | yes | — | — |
| **C** | yes | yes | — |
| **D** | yes | yes | yes |

An early benchmark in the series bundled B through D into a single condition and
consequently could not attribute an observed difference to material, to
execution, or to checking. Arms are also isolated: each works in a directory
containing only the task statement and its inputs, with reading outside that
directory and web search prohibited. §4.2.2 reports a case where this isolation
failed.

Not every benchmark carries all four arms; §4.2.5 gives the distribution and
restricts the cross-domain claims accordingly.

---

## 2.5 The eight domains

| Benchmark | Tasks | Arms | Domain | What is produced | Governing authority |
|---|---|---|---|---|---|
| `cad` | 4 | A B C | Architectural 2D drawing | A DXF file | National CAD drafting standard; a prefectural design-review checklist |
| `sekisan` | 6 | A B C | Quantity surveying | Quantities for interior finishes | Public Building Quantity Surveying Standard (2023) |
| `doboku` | 2 | A B C | Civil engineering CAD | An SXF (SFC) file | SXF Ver.3.1 specification; CAD drafting standard |
| `kanzei` | 4 | A B C D | Customs classification | A 9-digit import statistical code | Japan Customs advance rulings; tariff schedule and explanatory notes |
| `jiban` | 2 | A B C D | Geotechnical assessment | FL and PL values per depth | Specifications for Highway Bridges V (2017); KuniJiban borehole data |
| `kikai` | 2 | B C | Mechanical tolerancing | Extracted geometric tolerances and datums | STEP AP242 semantic PMI; NIST PMI definitions |
| `bim` | 2 | B C | Building information modelling | Spatial structure, element assignment, quantities | IFC; buildingSMART sample models |
| `zeimu` | 2 | A B C | Tax law | The statutory provisions relied upon | National Tax Agency published Q&A |

Two properties of this set are worth noting. Seven of the eight are governed by
Japanese instruments, which is why they are unoccupied by existing work and also
why generalisation is limited (§4.3.3). And the tasks divide into **generation**
(`cad`, `doboku`, `sekisan`, `jiban`), **extraction** (`kikai`, `bim`) and
**classification or identification** (`kanzei`, `zeimu`) — a division that
§3.2.1 suggests may track the sign of the material effect, though eight domains
cannot settle it.

## 2.6 What "33 tasks" counts

The count is of released task directories, and it mixes two things that should
be separated when reading the evidence. **Twenty-five are distinct questions.**
The remaining **eight are variants that hold the question fixed and vary exactly
one factor**: three in `kikai` and two in `bim` vary an examination-side
property of the task statement or answer format (§3.1.10, §3.1.6), two in
`kanzei` vary the size of the supplied material and the checker, and one in
`zeimu` is the same question re-issued to measure run-to-run variance.

The variants are not padding, and they are not independent evidence either.
Every controlled comparison in §3.1.10 and §3.2.1 depends on them, because the
only way to attribute a score change to one factor is to change one factor. But
a reader estimating how much of professional practice this series covers should
use 25, not 33. Earlier releases of this paper reported 24 without stating a
rule; that number is superseded by the rule above rather than by a correction to
it, since the series has grown since.

## 2.7 Experimental setup

The benchmark harness did not record the identity of the system executing the
arms. Token counts, durations and tool-use counts were captured per run; the
model was not. It was ambient context at the time of execution and was treated
as too obvious to write down — which is, in miniature, the failure this paper is
about.

The identity has been **reconstructed after the fact** from the operator's
session logs. That reconstruction is reported here in full, including where it
fails.

| | |
|---|---|
| Arm invocations traced | 106, across three sessions |
| Model of the invoking session | `claude-opus-5` in all three |
| Per-arm model override | none; all 106 inherited the session model |
| Arm invocations **not** traced | `cad-bench` — all rounds |
| Version or snapshot beyond the family identifier | not recorded |
| Sampling parameters | not recorded |
| Period of execution | 2026-07 to 2026-08 |

For seven of the eight benchmarks the arms therefore ran on `claude-opus-5`,
subject to the caveat that this is inferred from the invoking session rather
than logged by the harness. For `cad-bench` it could not be established: those
runs predate the traced sessions, and the operator's logs from that period show
two different models in concurrent use, so no assumption is available.

**What this permits and forbids.** §3.1 is unaffected: which system reported a
defect does not bear on whether the defect was real, and every defect counted
was confirmed on review. §3.2 is affected, and its claims should be read as
holding for one unspecified snapshot of one model family. Statements involving
`cad-bench` carry the additional caveat that the executing model is unknown;
`cad-bench` contributes to none of the claims in §3.2.

Neither the reconstruction nor its gaps should be taken as adequate. A
contemporaneous record is what is required, and its absence here is a defect in
the study on the same footing as those reported in §3.1.3.

## 2.8 What is measured

Each benchmark scores on a ladder rather than a single figure, so that partial
competence is visible: whether the output parses at all, whether the right scope
was selected, whether intermediate quantities agree, whether the final judgement
agrees. Ladder composition is domain-specific and is documented in each
repository.

Alongside score, each run records tokens consumed, wall-clock duration and tool
invocations. Cost is supplied by the harness that runs the arm rather than
computed by the benchmark, since the benchmark cannot observe it; where cost is
absent the score is still reported. §3.2.2 is the reason this instrumentation
exists, and §4.4 notes that it has been exercised in only three of the eight
domains.
