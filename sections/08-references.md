# References

Confirmed against the source records on 2026-08-09. Entries marked *(unverified)*
could not be resolved to a citable identifier and are cited in the text by name
only; they must be either resolved or removed before submission.

## Ground-truth errors in benchmarks (§3.1, §5.1)

[1] C. G. Northcutt, A. Athalye and J. Mueller.
**Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks.**
*Proceedings of the 35th Conference on Neural Information Processing Systems
(NeurIPS 2021), Track on Datasets and Benchmarks.*
arXiv:2103.14749. https://arxiv.org/abs/2103.14749

[2] A. P. Gema, J. O. J. Leang, G. Hong, A. Devoto, A. C. M. Mancino, R. Saxena,
X. He, Y. Zhao, X. Du, M. R. G. Madani, C. Barale, R. McHardy, J. Harris,
J. Kaddour, E. van Krieken and P. Minervini.
**Are We Done with MMLU?**
*NAACL 2025.* arXiv:2406.04127. https://arxiv.org/abs/2406.04127
Dataset: `edinburgh-dawg/mmlu-redux`

[3] D. Chong, J. Hong and C. D. Manning.
**Detecting Label Errors by using Pre-Trained Language Models.**
*EMNLP 2022.* https://nlp.stanford.edu/pubs/chong2022labelerrors.pdf

## Reliability under repetition (§3.2.3, §5.3)

[4] S. Yao, N. Shinn, P. Razavi and K. Narasimhan.
**τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains.**
arXiv:2406.12045. https://arxiv.org/abs/2406.12045
Code: https://github.com/sierra-research/tau-bench

## Multi-metric evaluation (§3.2.2, §5.4)

[5] P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, M. Yasunaga et al.
**Holistic Evaluation of Language Models.**
*Transactions on Machine Learning Research*, August 2023.
arXiv:2211.09110. https://arxiv.org/abs/2211.09110

## Retrieval augmentation (§3.2.1, §5.1)

[5a] **Evaluating the Effectiveness and Scalability of LLM-Based Data
Augmentation for Retrieval.**
arXiv:2509.16442. https://arxiv.org/abs/2509.16442
*Cited for the finding that augmentation improves recall broadly while
degrading ranking metrics for some task categories, and that benefits saturate
with scale.*

## Domain benchmarks — customs classification (§5.2)

[6] P. Yuvraj and S. Devarakonda.
**ATLAS: Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff
Code Classification.**
arXiv:2509.18400. https://arxiv.org/abs/2509.18400

[7] **HSCodeComp: A Realistic and Expert-level Benchmark for Deep Search Agents
in Hierarchical Rule Application.**
arXiv:2510.19631. https://arxiv.org/abs/2510.19631
Dataset: `AIDC-AI/HSCodeComp`

[8] B. Judy.
**Benchmarking Harmonized Tariff Schedule Classification Models.**
arXiv:2412.14179. https://arxiv.org/abs/2412.14179

[9] **NoRMA: A Multi-agent Communication-Centric Dataset for Enhanced Customs
Nomenclature Classification.**
Springer, Lecture Notes in Computer Science.
https://doi.org/10.1007/978-3-032-15632-7_18

## Domain benchmarks — architecture, engineering, construction (§5.2)

[10] B. K. Nithyanantham, C. Kujat, T. Sesterhenn, S. Telgmann, A. Nedungadi,
J. Plönnigs, C. Bartelt and S. Lüdtke.
**BIM-Edit: Benchmarking Large Language Models for IFC-Based Building
Information Modeling.**
arXiv:2606.20146. https://arxiv.org/abs/2606.20146

[11] A. Kondratenko, M. Birhane, H. E. Hsain and G. Maciocci.
**AECV-Bench: Benchmarking Multimodal Models on Architectural and
Engineering Drawings Understanding.**
arXiv:2601.04819. https://arxiv.org/abs/2601.04819

[12] **AP242 Benchmark.** AFNET / ePLM Interoperability Forum.
http://benchmark.ap242.org/
*Cited only to distinguish it: it certifies interoperability between PLM
products and is not a language-model evaluation.*

## Japanese-language evaluation (§1.2, §5.2)

[13] **JMMLU: Japanese Massive Multitask Language Understanding Benchmark.**
Waseda University NLP Laboratory. https://github.com/nlp-waseda/JMMLU

[14] **JMED-LLM: Japanese Medical Evaluation Dataset for Large Language Models.**
Social Computing Laboratory, NAIST. https://github.com/sociocom/JMED-LLM

[15] J. Jiang, J. Huang and A. Aizawa.
**JMedBench: A Benchmark for Evaluating Japanese Biomedical Large Language
Models.** arXiv:2409.13317. https://arxiv.org/abs/2409.13317
*Cited as the collecting reference for IgakuQA and JMMLU-medical.*

## Standards and data sources (§2, §7)

[16] 日本道路協会 (Japan Road Association).
**道路橋示方書・同解説 V 耐震設計編** (Specifications for Highway Bridges,
Part V: Seismic Design). November 2017.

[17] 土木研究所 (Public Works Research Institute).
**細粒分を含む砂の液状化強度の評価法に関する再検討.**
土木研究所資料 第4352号.
https://www.pwri.go.jp/team/smd/pdf/report4352.pdf

[18] 岩崎敏男, 龍岡文夫, 常田賢一, 安田進.
**地震時地盤液状化の程度の予測について.**
*土と基礎* 28(4), pp. 23–29, 1980.

[19] 国土交通省・土木研究所・港湾空港技術研究所.
**国土地盤情報検索サイト KuniJiban.** https://www.kunijiban.pwri.go.jp/

[20] 国土交通省. **公共建築数量積算基準** (2023 revision).
https://www.mlit.go.jp/common/001178206.pdf

[21] 国土交通省 CALS/EC. **SXF Ver.3.1 仕様書・同解説（第2版）.**
https://www.cals-ed.go.jp/sxf_ver3-1_specification_draft/

[22] buildingSMART International Ltd. **Sample-Test-Files.** CC BY 4.0.
https://github.com/buildingSMART/Sample-Test-Files

[23] National Institute of Standards and Technology / MBx Interoperability Forum.
**MBE PMI Validation and Conformance Testing Project.**
https://www.mbx-if.org/home/cax/resources/

[24] 国税庁 (National Tax Agency). **質疑応答事例.**
https://www.nta.go.jp/law/shitsugi/

[25] 税関 (Japan Customs). **事前教示回答（品目分類）.**
https://www.customs.go.jp/

## Benchmarks described in this paper (§7)

[26] B. Ohkubo. **jiban-bench.** https://doi.org/10.5281/zenodo.21847239
[27] B. Ohkubo. **doboku-bench.** https://doi.org/10.5281/zenodo.21847241
[28] B. Ohkubo. **sekisan-bench.** https://doi.org/10.5281/zenodo.21847243
[29] B. Ohkubo. **zeimu-bench.** https://doi.org/10.5281/zenodo.21847245
[30] B. Ohkubo. **kikai-bench.** https://doi.org/10.5281/zenodo.21847247
[31] B. Ohkubo. **bim-bench.** https://doi.org/10.5281/zenodo.21847249
[32] B. Ohkubo. **kanzei-bench.** https://doi.org/10.5281/zenodo.21847251
[33] B. Ohkubo. **cad-bench.** https://doi.org/10.5281/zenodo.21847358

---

## Outstanding

- **[6]** — the second author is recorded here as S. Devarakonda from a
  secondary source. It has not been confirmed against the paper itself and
  should be before any venue submission.
- **IgakuQA119** is cited in §1.2 by name and is reached here through [15].
  Its own citable record has not been located; if one exists it should replace
  the indirect citation.
- Reference numbering uses **[5a]** for the retrieval-augmentation entry so that
  the existing numbers are not disturbed. Renumber when the manuscript is
  finalised for a specific venue.
