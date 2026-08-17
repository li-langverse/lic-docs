#!/usr/bin/env python3
"""Publish llms.txt, llms-full.txt, and raw markdown for AI agents and chats."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"
BASE = "https://docs.lilangverse.xyz"
RAW = f"{BASE}/raw"

# First-paragraph blurbs for the index. Keep in sync with the page lead.
BLURBS: dict[str, str] = {
    "for-agents.md": "How agents and chats should fetch this handbook.",
    "getting-started.md": "What Li is, and the first commands.",
    "guide/hello-world.md": "A first program with requires / ensures / decreases.",
    "guide/getting-started-tools.md": "Install lic and the toolchain.",
    "guide/fast-math-and-parallelism.md": "SIMD and parallel for, after the check.",
    "guide/math-hpc-examples.md": "Math-first examples for HPC.",
    "guide/examples-gallery.md": "Copy-paste examples.",
    "guide/creating-packages.md": "Scaffold a package with li-new-package.",
    "guide/package-layout-reference.md": "Package layout on disk.",
    "language/overview.md": "Handbook map: types, numbers, SIMD, contracts.",
    "language/philosophy.md": "Why Li is written the way it is.",
    "language/types-and-data.md": "Types and data. No Any.",
    "language/contracts-and-proofs.md": "requires, ensures, decreases.",
    "language/numerics.md": "Numbers and numeric policy.",
    "language/simd-parallel.md": "Vectors and parallel for.",
    "language/li-toml.md": "The package manifest.",
    "compiler/build-pipeline.md": "How a file becomes a binary.",
    "compiler/why-provable.md": "Why the compiler refuses unproved programs.",
    "compiler/llvm-abi.md": "LLVM ABI notes.",
    "architecture/overview.md": "Compiler architecture.",
    "verification/overview.md": "Verification surface.",
    "verification/provability-gaps.md": "Honest today-vs-target register. Read before claiming proofs.",
    "verification/proof-corpus-roadmap.md": "Proof corpus plan.",
    "testing/overview.md": "Test suites and CI.",
    "testing/security.md": "Security audits.",
    "ecosystem/overview.md": "Packages, lip, governance.",
    "ecosystem/agent-handover-formats.md": "How agents should discover tools and errors.",
    "ecosystem/ADOPTION.md": "Agent-kit adoption.",
    "contributing/documentation.md": "How to write handbook pages.",
    "superpowers/specs/2026-05-14-li-language-design.md": "Normative language design.",
    "superpowers/plans/2026-05-14-li-master-plan.md": "Phase tracker.",
    "benchmarks.md": "Benchmark notes.",
}

# Concatenated into llms-full.txt. Keep this short enough to load in a chat.
FULL_PAGES: list[str] = [
    "for-agents.md",
    "getting-started.md",
    "guide/hello-world.md",
    "guide/getting-started-tools.md",
    "language/overview.md",
    "language/philosophy.md",
    "language/types-and-data.md",
    "language/contracts-and-proofs.md",
    "language/numerics.md",
    "language/simd-parallel.md",
    "compiler/why-provable.md",
    "compiler/build-pipeline.md",
    "verification/provability-gaps.md",
    "ecosystem/agent-handover-formats.md",
    "ecosystem/overview.md",
    "contributing/documentation.md",
]

SKIP_RAW_PREFIXES = (
    "release-notes/",
    "reports/",
    "demo/",
    "numerics/studies/",
    "superpowers/plans/2026-05-14-phase-",
    "game-dev/specs/",
    "ecosystem/research-sessions/",
    "ecosystem/orchestrator-notes/",
    "ecosystem/stdlib-research/",
)

SECTIONS: list[tuple[str, list[str]]] = [
    (
        "Start here",
        [
            "for-agents.md",
            "getting-started.md",
            "guide/hello-world.md",
            "guide/getting-started-tools.md",
            "verification/provability-gaps.md",
        ],
    ),
    (
        "Language",
        [
            "language/overview.md",
            "language/philosophy.md",
            "language/types-and-data.md",
            "language/contracts-and-proofs.md",
            "language/numerics.md",
            "language/simd-parallel.md",
            "language/li-toml.md",
            "guide/math-hpc-examples.md",
            "guide/examples-gallery.md",
        ],
    ),
    (
        "Compiler and proof",
        [
            "compiler/why-provable.md",
            "compiler/build-pipeline.md",
            "verification/overview.md",
            "testing/overview.md",
        ],
    ),
    (
        "Agents",
        [
            "ecosystem/agent-handover-formats.md",
            "ecosystem/ADOPTION.md",
            "ecosystem/overview.md",
        ],
    ),
    (
        "Optional",
        [
            "contributing/documentation.md",
            "superpowers/specs/2026-05-14-li-language-design.md",
            "superpowers/plans/2026-05-14-li-master-plan.md",
            "benchmarks.md",
        ],
    ),
]


def first_heading(text: str) -> str:
    text = text.lstrip("\ufeff")
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return ""


def blurb_for(rel: str, text: str) -> str:
    if rel in BLURBS:
        return BLURBS[rel]
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("<") or s.startswith("<!--"):
            continue
        if s.startswith(">") or s.startswith("|") or s.startswith("```"):
            continue
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
        return s[:180]
    return "Handbook page."


def write_llms_txt() -> str:
    lines = [
        "# Li",
        "",
        "> A compiled language for science and simulation. You write ordinary code,",
        "> then you write what has to stay true. If that does not hold, Li will not",
        "> give you a program. HTML: https://docs.lilangverse.xyz/ — fetch Markdown from /raw/.",
        "",
        f"Full text: {BASE}/llms-full.txt",
        f"This index: {BASE}/llms.txt",
        f"Source: https://gitlab.lilangverse.xyz/li-langverse/lic-docs",
        "",
    ]
    for title, pages in SECTIONS:
        lines.append(f"## {title}")
        lines.append("")
        for rel in pages:
            path = DOCS / rel
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            name = first_heading(text) or Path(rel).stem.replace("-", " ")
            lines.append(f"- [{name}]({RAW}/{rel}): {blurb_for(rel, text)}")
        lines.append("")
    lines.append("## Also")
    lines.append("")
    lines.append(f"- [Agent manifest (TOML)]({RAW}/ecosystem/li-agent-manifest.toml): commands agents should run.")
    lines.append(f"- [Diagnostic schema]({BASE}/schemas/diagnostic-v1.json): `lic check --format=json` / `lic diagnose`.")
    lines.append("")
    return "\n".join(lines)


def write_llms_full() -> str:
    parts = [
        "# Li — curated handbook for agents",
        "",
        "> Fetch https://docs.lilangverse.xyz/llms.txt first if you only need the map.",
        "> Read verification/provability-gaps.md before claiming what lic build proves.",
        "",
    ]
    for rel in FULL_PAGES:
        path = DOCS / rel
        if not path.is_file():
            continue
        body = path.read_text(encoding="utf-8", errors="replace").strip()
        parts.append(f"\n\n<!-- source: {rel} -->\n\n{body}\n")
    return "".join(parts).strip() + "\n"


def copy_raw() -> int:
    dest_root = SITE / "raw"
    dest_root.mkdir(parents=True, exist_ok=True)
    n = 0
    for path in DOCS.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(DOCS).as_posix()
        if rel.startswith(SKIP_RAW_PREFIXES):
            continue
        if path.suffix not in {".md", ".toml", ".json", ".li"}:
            continue
        if path.name == "robots.txt":
            continue
        out = dest_root / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(path.read_bytes())
        n += 1
    index = [
        "# Raw handbook files",
        "",
        "Fetch a page as Markdown from this tree. Example:",
        f"`{RAW}/guide/hello-world.md`",
        "",
        f"Index: {BASE}/llms.txt",
        "",
    ]
    (dest_root / "README.md").write_text("\n".join(index), encoding="utf-8")
    return n


def main() -> None:
    if not SITE.is_dir():
        raise SystemExit(f"missing site dir: {SITE} (run mkdocs build first)")
    (SITE / "llms.txt").write_text(write_llms_txt(), encoding="utf-8")
    (SITE / "llms-full.txt").write_text(write_llms_full(), encoding="utf-8")
    robots = DOCS / "robots.txt"
    if robots.is_file():
        (SITE / "robots.txt").write_bytes(robots.read_bytes())
    n = copy_raw()
    print(f"agent-docs: llms.txt llms-full.txt robots.txt raw/{n} files")


if __name__ == "__main__":
    main()
