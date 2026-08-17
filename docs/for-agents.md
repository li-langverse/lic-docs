# For agents and chats

This handbook is for people and for agents. Do not scrape the HTML. Fetch the markdown.

## Start here

| File | What it is |
|------|------------|
| [llms.txt](https://docs.lilangverse.xyz/llms.txt) | Curated index. Fetch this first. |
| [llms-full.txt](https://docs.lilangverse.xyz/llms-full.txt) | The same core pages, concatenated. |
| [raw/](https://docs.lilangverse.xyz/raw/) | One page at a time, as Markdown. Example: [raw/guide/hello-world.md](https://docs.lilangverse.xyz/raw/guide/hello-world.md). |
| [robots.txt](https://docs.lilangverse.xyz/robots.txt) | Allows crawlers; points at `llms.txt` and the sitemap. |

HTML lives at the same path without `raw/` and without `.md`. GitLab source of truth: [li-langverse/lic-docs](https://gitlab.lilangverse.xyz/li-langverse/lic-docs).

## Read before you claim what Li does

1. [Provability gaps](verification/provability-gaps.md) — **today** vs **target**. `lic build` is not a Lean certificate yet.
2. [Agent handover formats](ecosystem/agent-handover-formats.md) — how Li expects agents to work in a repo.
3. [li-agent-manifest.toml](ecosystem/li-agent-manifest.toml) — commands to run (`lic check`, `lic diagnose`, tests).
4. [Documentation style](contributing/documentation.md) — do not invent features; do not skip the gap register.

## Suggested ingest

```text
1. GET https://docs.lilangverse.xyz/llms.txt
2. If the task is small, GET the linked raw/*.md pages you need.
3. If the task is “learn Li” or you have budget, GET llms-full.txt.
4. Before writing code or promising proofs, GET raw/verification/provability-gaps.md.
```

In a clone of this repo, read `docs/` directly. Do not paste secrets, tokens, or `.env` files into a chat.

## What not to do

- Do not treat the styled HTML as the source. The source is Markdown.
- Do not say `lic build` runs Lean or closes all proofs unless the gap page says that row is closed.
- Do not copy ten-page tables from the design spec into a prompt when a link will do.
- Release notes and daily reports are optional; they are not in `llms-full.txt` on purpose.

## Related

- [Language handbook](language/overview.md)
- [Hello world](guide/hello-world.md)
- [LLM-first design (research)](superpowers/specs/2026-05-16-li-llm-first-design.md)
- [Diagnostic schema](schemas/diagnostic-v1.json)
