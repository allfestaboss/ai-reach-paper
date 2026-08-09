# ai-reach-paper

「AI実務到達度インデックス」の方法論論文。8本のベンチマークを横断して得た所見と、
その過程で見つかったベンチマーク自身の欠陥についての報告。

**Title (working):** Who checks the answer key? Ground-truth defects in eight
professional-practice benchmarks

## 主張

> ベンチマークの検査（採点器・較正・敵対テスト）はすべて参照解を基準に定義されている。
> だから参照解の誤りだけは、原理的に検出できない。
> 実際に見つけたのは被験者だった —— 15件中14件。

副次的に、既知の3効果（資料を渡す効果／飽和後のコスト／反復の非決定性）が
業種でどれだけ変わるかを、同一設計のもとで測っている。

## 構成

```
00-abstract-and-title.md    Abstract（フル版と投稿版）、タイトル案、重心の記録
sections/
  01-introduction.md        既存ベンチの4分類と、この研究の位置
  02-design.md              設計原則4つ、8業種の一覧、実験設定
  03-findings.md            §3.1 参照解の検証不能性（主）／§3.2 業種差の測定
  04-threats.md             Construct / Internal / External / 未解決
  05-related-work.md        先行研究との差分、§5.5 に主張の棚卸し表
  06-discussion.md          符号反転の仮説、解答者を監査に組み込む設計
  07-availability.md        DOI 9本と、同梱しないデータの理由
refs/
  outline-v0.1.html         最初の構成案
  test0-prior-work.html     先行研究の潰し込み（Test 0）
  review-v2.html            査読 第2回（10件中8件解消）
```

## 対象となるベンチマーク

| Benchmark | Concept DOI |
|---|---|
| jiban-bench | 10.5281/zenodo.21847239 |
| doboku-bench | 10.5281/zenodo.21847241 |
| sekisan-bench | 10.5281/zenodo.21847243 |
| zeimu-bench | 10.5281/zenodo.21847245 |
| kikai-bench | 10.5281/zenodo.21847247 |
| bim-bench | 10.5281/zenodo.21847249 |
| kanzei-bench | 10.5281/zenodo.21847251 |
| cad-bench | 10.5281/zenodo.21847358 |

## 状態

- [x] 全8章の初稿（約11,300語）
- [x] 先行研究の潰し込み（Test 0）— 主張を2回、狭める方向に修正した
- [x] 査読1回目（致命的2・重大4・軽微4）→ 修正 → 査読2回目（8件解消）
- [x] 実験設定の復元（腕106回ぶん、`claude-opus-5`。cad-bench のみ不明）
- [x] 節参照の整合、章をまたぐ数値の整合、DOI 9本の照合
- [ ] **参考文献リスト**（本文で13件を名前で挙げているが書誌が無い）
- [ ] 1本の文書への組み上げ
- [ ] 投稿先の決定（cs.SE を想定）

## 投稿先について

**cs.SE を想定している。** 主張が「ベンチマークという成果物の検証可能性」であり、
評価対象がモデルではなく測定器そのものだから。cs.CL に出すと
「どのモデルが強いのか」という読まれ方をされやすく、この論文はそこに答えない。

## ライセンス

本文は CC BY 4.0。対象ベンチマークのコードは各リポジトリの MIT に従う。
