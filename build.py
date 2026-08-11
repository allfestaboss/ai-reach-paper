#!/usr/bin/env python3
"""節を1本の原稿に組み上げる。

00-abstract-and-title.md には作業メモ（重心の記録、案の比較、波及の一覧）が
混ざっている。原稿に入れるのはタイトルと投稿版 Abstract だけなので、
ここで抜き出す。手で消すと、次に Abstract を直したとき同期が切れる。

出力:
  build/paper.md   投稿用の本文（作業メモを含まない）
  build/paper.html 素の HTML（pandoc が無い環境でも読める）
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "build"

SECTIONS = [
    "01-introduction.md",
    "02-design.md",
    "03-findings.md",
    "04-threats.md",
    "05-related-work.md",
    "06-discussion.md",
    "07-availability.md",
    "08-references.md",
]


def front_matter() -> str:
    """タイトルと投稿版 Abstract を 00 から抜き出す。"""
    src = (ROOT / "00-abstract-and-title.md").read_text(encoding="utf-8")

    m = re.search(r"^\*\*Title\*\*\s*\n\n> (.+?)\n\n", src, re.S | re.M)
    if not m:
        raise SystemExit("タイトルが見つからない。00 の書式が変わっている")
    title = " ".join(x.strip("> ").strip() for x in m.group(1).split("\n"))

    m = re.search(r"## Abstract — 投稿版[^\n]*\n+(.*?)\n+(?=\*\(|## |---)", src, re.S)
    if not m:
        raise SystemExit("投稿版 Abstract が見つからない。00 の書式が変わっている")
    abstract = m.group(1).strip()

    return (
        f"# {title}\n\n"
        "Boss Ohkubo (Allfesta Corp.)  \n"
        "ORCID 0009-0007-8300-0039\n\n"
        "## Abstract\n\n"
        f"{abstract}\n"
    )


def body() -> str:
    out = []
    for name in SECTIONS:
        p = ROOT / "sections" / name
        if not p.exists():
            raise SystemExit(f"欠落: {name}")
        out.append(p.read_text(encoding="utf-8").rstrip())
    return "\n\n---\n\n".join(out)


def to_html(md: str, title: str) -> str:
    """依存を足さずに読める形にする。整形が目的で、厳密な変換ではない。"""
    lines, out, in_code, in_table = md.split("\n"), [], False, False

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    for ln in lines:
        if ln.startswith("```"):
            in_code = not in_code
            out.append("<pre>" if in_code else "</pre>")
            continue
        if in_code:
            out.append(html.escape(ln))
            continue
        if ln.startswith("|"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            if not in_table:
                out.append("<table>")
                in_table = True
                out.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells) + "</tr>")
            else:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
            continue
        if in_table:
            out.append("</table>")
            in_table = False
        if m := re.match(r"^(#{1,4}) (.+)", ln):
            n = len(m.group(1))
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif ln.startswith("> "):
            out.append(f"<blockquote>{inline(ln[2:])}</blockquote>")
        elif re.match(r"^[-*] ", ln):
            out.append(f"<li>{inline(ln[2:])}</li>")
        elif ln.strip() == "---":
            out.append("<hr>")
        elif ln.strip():
            out.append(f"<p>{inline(ln)}</p>")
    if in_table:
        out.append("</table>")

    css = """body{max-width:46em;margin:3em auto;padding:0 1.5em;
  font:16px/1.75 "Hiragino Kaku Gothic ProN","Yu Gothic",system-ui,sans-serif;color:#1a2a2c}
h1{font-size:1.8em;line-height:1.3}h2{margin-top:2em;border-bottom:1px solid #ccc;padding-bottom:.3em}
h3{margin-top:1.6em}h4{margin-top:1.2em;font-size:1em}
pre{background:#f4f2ec;padding:1em;overflow-x:auto;font-size:.85em;border:1px solid #ddd}
code{background:#f4f2ec;padding:1px 4px;font-size:.9em}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.9em;display:block;overflow-x:auto}
th,td{border:1px solid #ccc;padding:.5em .7em;text-align:left}th{background:#f4f2ec}
blockquote{border-left:3px solid #1f5c55;margin:1em 0;padding:.3em 1em;color:#555}
hr{border:0;border-top:1px solid #ddd;margin:2.5em 0}li{margin:.3em 0}"""
    return (f"<!doctype html><meta charset=utf-8><title>{html.escape(title)}</title>"
            f"<style>{css}</style>\n" + "\n".join(out))


def main() -> None:
    OUT.mkdir(exist_ok=True)
    fm = front_matter()
    md = fm + "\n---\n\n" + body() + "\n"
    (OUT / "paper.md").write_text(md, encoding="utf-8")

    title = re.match(r"# (.+)", fm).group(1)
    (OUT / "paper.html").write_text(to_html(md, title), encoding="utf-8")

    words = len(re.findall(r"[A-Za-z0-9'’\-]+", md))
    print(f"  build/paper.md    {len(md):>7,} 文字 / 約{words:,}語")
    print(f"  build/paper.html  {(OUT / 'paper.html').stat().st_size:>7,} バイト")
    print(f"  タイトル: {title}")


if __name__ == "__main__":
    main()

def check_versions():
    """CITATION.cff と .zenodo.json の版がズレたまま公開すると、
    **Zenodo は .zenodo.json のほうを採る。**実際に v1.3.0 を 1.2.1 として
    登録させた。ここで落とす。"""
    import json, yaml
    cff = yaml.safe_load(open("CITATION.cff"))["version"]
    zen = json.load(open(".zenodo.json")).get("version")
    if zen is not None and zen != cff:
        raise SystemExit(
            f"版がズレている。CITATION.cff={cff} / .zenodo.json={zen}\n"
            f"  **このまま release を切ると Zenodo は {zen} として登録する。**")
    print(f"  版の一致        CITATION.cff = .zenodo.json = {cff}")


check_versions()
