# 5. Related work

## 5.1 Errors in benchmark ground truth

That widely used benchmarks contain incorrect ground truth is established.
Northcutt et al. examined the test sets of ten commonly used vision, language
and audio datasets and estimated an average of at least 3.3 percent label
errors, with at least 6 percent in the ImageNet validation set. Candidates were
identified by confident learning and then validated by crowdworkers, of whom
roughly half confirmed each flagged instance. They further showed that the
errors are consequential for model selection: on corrected ImageNet labels,
ResNet-18 overtakes ResNet-50 once the prevalence of originally mislabelled test
examples rises by six points.

For language models specifically, MMLU-Redux re-annotated 5,700 MMLU questions
across all 57 subjects and reported an error rate of roughly 6.5 percent
overall, with extreme variance by subject — near zero in physics against 57
percent in virology — and introduced a taxonomy separating wrong ground truth,
multiple correct options and unclear questions. Related work has used
pre-trained language models themselves as label-error detectors.

**This body of work and ours address different failure modes, and the
distinction determines which detection methods can apply.**

| | Prior work | This work |
|---|---|---|
| Where the error lives | An **annotation** attached to an instance | The **program** that derives the reference from external sources |
| Distribution | **Sparse and idiosyncratic** across instances | **Systematic** — every instance on the same code path is wrong in the same direction |
| Detection | Confident learning, model disagreement, or human re-annotation; post hoc, at dataset scale | Reported by a solver during ordinary operation |

The methods that succeed on sparse annotation errors do not transfer. Confident
learning identifies instances where a model trained on the dataset confidently
disagrees with the label; it depends on the errors being rare relative to a
correct majority that supplies the signal. A defect in a reference
*implementation* is not rare in that sense. In §3.1.2, every case computed by
the affected code path is displaced by the same mechanism, so there is no clean
subset to disagree with — and systematic disagreement between models and the
reference is exactly what a benchmark is designed to interpret as *the models
being wrong*.

Human re-annotation does not transfer either, for a different reason. A
re-annotator of MMLU can read a question and know the answer. A re-annotator of
a liquefaction assessment must execute the standard over the borehole data,
which is to reimplement the reference — and will reproduce a misreading of the
standard's integration bounds as readily as the original did. Independent
reimplementation would help; independent *inspection* of the reference by the
same route would not.

What the solvers supplied was neither. They reasoned from the raw input and
observed that the borehole record ended before the integration did — an
observation available only to something looking at that instance's inputs, and
not derivable from any statistic over the dataset.

We do not claim that reference errors are novel, nor that using models to find
them is novel. We claim that **systematic errors in computed reference solutions
are a distinct class**, that the established detection methods are structurally
unable to reach them, and that in this series the only detector that
located them was the subject under test (§3.1).

## 5.2 Professional and domain-specific benchmarks

Examination-derived benchmarks — MMLU and its Japanese counterparts JMMLU,
JMED-LLM and IgakuQA119 — take ground truth from an examining body and pose
selection among options. They establish knowledge coverage and do not require
that anything be produced.

Single-domain suites evaluate professional artefacts against external
authorities. ATLAS fine-tunes on 18,731 United States customs rulings and
reports 40 percent exact agreement at ten digits; HSCodeComp supplies 632
expert-annotated entries across 27 chapters; NoRMA contributes 3,424 curated
entries from Moroccan customs. BIM-Edit provides 324 natural-language editing
tasks over 11 real and 36 synthetic IFC models. AECV-Bench evaluates multimodal
understanding of architectural and engineering drawings.

Our customs and BIM benchmarks are substantially smaller than the corresponding
prior work — four and two tasks against 18,731 rulings and 324 tasks — and are
not competitive as measurements of those tasks in isolation (§4.3.5). They are
included because a cross-domain comparison requires the same design in every
domain, and because the defect record in §3.1.3 comes from the customs
benchmark.

The AP242 Benchmark maintained by AFNET shares a name with our mechanical
benchmark but addresses a different question: it certifies interoperability
between PLM products, not the ability of a language model to read semantic PMI.

## 5.3 Reliability under repetition

τ-bench introduced `pass^k`, the probability that all of k repeated runs
succeed, and demonstrated the gap it exposes between average and worst-case
behaviour — 61 percent at pass@1 against 25 percent at pass@8 for one system on
retail agent tasks. The metric has been widely adopted, including in model
cards, and subsequent work has extended reliability evaluation to long-horizon
tasks and to production-like stress conditions.

§3.2.3 measures the same axis across eight domains rather than within one, and
reports one pattern the metric cannot represent. `pass^k` reduces each trial to
success or failure. Where the answer is a set — the statutory provisions relied
upon, in `zeimu` — a case can score identically on five runs while returning a
different set each time, by exchanging one correct element for another. Half the
unstable cases in that benchmark behave this way. A binary success criterion
records them as five identical outcomes.

## 5.4 Cost and multi-metric evaluation

HELM measures seven metrics for every scenario — accuracy, calibration,
robustness, fairness, bias, toxicity and efficiency — expressly so that
trade-offs are not concealed behind a headline number, and cost per task now
appears as a standard column on public leaderboards. Efficiency-focused
evaluation arenas standardise the measurement further.

§3.2.2 does not propose measuring cost. It reports what cost does at the point
where accuracy has stopped discriminating: in one domain, configurations tied at
100 out of 100 across two task sizes while their unit-cost gap widened from 1.37
to 2.6 times. The observation requires the accuracy axis to be saturated before
the cost axis is read, which is a condition rarely reported because saturated
tasks are usually retired rather than instrumented. §3.2.2 states why we make
this claim for one domain only.

## 5.5 Summary of position

| Claim | Novel? | Nearest prior work |
|---|---|---|
| Benchmarks contain ground-truth errors | **No** | Northcutt et al.; MMLU-Redux |
| Models can be used to find such errors | **No** | Confident learning; PLM-based detection |
| **Systematic errors in computed references are a distinct class that those methods cannot reach** | **Yes** | — |
| **In this design the solvers were the only detector that located them, 14 of 15** | **Yes** | — |
| Retrieval and augmentation help unevenly, sometimes negatively | **No** | Retrieval augmentation literature |
| Reliability under repetition is an evaluation axis | **No** | τ-bench and successors |
| **A stable score can conceal a churning answer set; `pass^k` cannot express it** | **Yes** | — |
| Efficiency belongs alongside accuracy | **No** | HELM |
| **At tied scores, the cost gap widens with task size** (one domain, two sizes) | **Partly** | — |
| Professional-practice benchmarks in these Japanese domains | **Yes**, six of eight | ATLAS, BIM-Edit for the other two |
