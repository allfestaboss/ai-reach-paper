# 7. Availability

All eight benchmarks are released in full under the MIT licence, each with a
persistent identifier. Every repository contains the tasks, the reference
implementation, the grader, the adversarial suite, the submissions of every arm
that was run, and the defect record where one exists.

| Benchmark | Domain | Concept DOI |
|---|---|---|
| `jiban-bench` | Geotechnical assessment | `10.5281/zenodo.21847239` |
| `doboku-bench` | Civil engineering CAD (SXF) | `10.5281/zenodo.21847241` |
| `sekisan-bench` | Quantity surveying | `10.5281/zenodo.21847243` |
| `zeimu-bench` | Tax provision identification | `10.5281/zenodo.21847245` |
| `kikai-bench` | Mechanical tolerancing (AP242) | `10.5281/zenodo.21847247` |
| `bim-bench` | Building information modelling (IFC) | `10.5281/zenodo.21847249` |
| `kanzei-bench` | Customs classification | `10.5281/zenodo.21847251` |
| `cad-bench` | Architectural 2D drawing (DXF) | `10.5281/zenodo.21847358` |

Each DOI above is a concept identifier resolving to the current version;
version-specific identifiers for the release described in this paper are
recorded in each repository's `CITATION.cff`. Source repositories are at
`github.com/allfestaboss/<name>`.

A related simulation used in one of the geotechnical analyses is archived
separately at `10.5281/zenodo.21833819`.

## 7.1 What is not bundled, and why

The design requires inputs and procedures to come from external authorities
(§2.1), and those authorities impose their own terms. Where redistribution is
permitted the material is included; where it could not be confirmed it is not,
and the acquisition route is documented instead. No benchmark depends on
non-bundled material to run: calibration, adversarial testing and scoring all
pass without it.

| Material | Status | Terms |
|---|---|---|
| KuniJiban borehole records (`jiban`) | **Bundled** | Reproduction, distribution and sale permitted with attribution; no copyright may be asserted over the data |
| buildingSMART sample IFC models (`bim`) | **Bundled** | CC BY 4.0 |
| NIST MBE PMI test files and definitions (`kikai`) | **Bundled** | No redistribution restriction; attribution requested |
| National Tax Agency Q&A corpus (`zeimu`) | **Bundled** | Government terms; commercial use permitted, attribution and disclosure of adaptation required |
| Japan Customs advance rulings (`kanzei`) | **Bundled** | Reproduction, transmission, translation and adaptation permitted, including commercially, with attribution |
| PWRI Technical Note 4352 (`jiban`) | **Not bundled** | Redistribution permission could not be confirmed. The equations required to reproduce the reference are transcribed with equation numbers in the repository |
| SXF Ver.3.1 specification (`doboku`) | **Not bundled** | Redistribution permission could not be confirmed |
| Official drawing examples (`doboku`) | **Not bundled** | Carry an explicit notice against use as actual design or construction drawings |
| Prefectural design-review checklist (`cad`) | **Not bundled** | Redistribution permission could not be confirmed |
| Specifications for Highway Bridges V (`jiban`), Public Building Quantity Surveying Standard (`sekisan`) | **Not bundled** | Published books; cited by article and clause |

The MIT licence covers code and prose only. Bundled data retains the terms
above, which are recorded per repository in a `NOTICE` file and, where the
provenance differs file by file, in a per-directory manifest.

## 7.2 Reproducing a result

Each repository exposes a single entry point that runs the checks in the order
§2.2 requires:

```
run.sh        # calibration → adversarial suite → scoring
```

If calibration fails, or if any adversarial case is accepted by the grader, no
score is emitted. Arm submissions are stored as data, so scores in this paper
can be recomputed without re-running any model. Cost figures are recorded by the
harness that executed each arm and are stored alongside the submissions; where
absent, scoring proceeds and the cost column is empty.

## 7.3 Defect records

Repositories in which examination-side defects were found carry the record: what
was wrong, who reported it, whether it was confirmed, and what changed. The
`kanzei` record covers fifteen defects across three rounds, the `jiban` record
covers four in a single round, and the `kikai` record covers one found by
replication (`kikai-bench/docs/T001n3.md`). Results computed before a correction
are marked as superseded rather than removed, so that the effect of each
correction on the reported figures can be traced.

Two corrections are large enough to note here. In `jiban`, correcting the
integration bound described in §3.1.2 changed one hole's reported index from
27.965 to 11.756, and correcting the fines-content extraction raised the number
of assessable points in that task from 36 to 52. Both predate the figures
reported in §3.2.

**The `kikai` defect has deliberately not been corrected.** Adding the missing
fields to the task statement would change the scores, and the six runs were
commissioned to measure cost, which requires the task to be identical across
them. The defect falls equally on all six, so the comparison in §3.2.2 is
unaffected; it costs every run the same 5.4 points.

It has since been addressed **without editing the task**, which is the pattern
the series settled on for defects discovered after answers exist. T001 stands as
issued, with its defect recorded; three successor tasks share its reference byte
for byte and repair the two disclosure routes in the 2×2 of §3.1.10. The figures
reported here are T001's and remain the uncorrected ones, labelled as such in the
repository, and the repaired scores are reported alongside rather than in place
of them.
