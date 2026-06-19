# lic-docs

Published documentation for the [Li](https://github.com/li-langverse/lic) language (`lic` compiler, handbook, plans, verification notes).

| | |
|---|---|
| **Live site** | [li-langverse.github.io/lic-docs](https://li-langverse.github.io/lic-docs/) |
| **Compiler repo** | [li-langverse/lic](https://github.com/li-langverse/lic) |
| **Custom domain** (optional) | `docs.yourdomain.com` — set in repo **Settings → Pages** and add a CNAME in DNS |

## Build locally

```bash
./scripts/build-docs.sh
python3 -m http.server -d site 8000   # preview at http://127.0.0.1:8000
```

Requires Python 3.10+.

## Edit workflow

1. Change Markdown under `docs/`.
2. Open a PR in **this repo** (`lic-docs`), not in `lic`.
3. CI builds with `mkdocs --strict` on push to `main` and deploys GitHub Pages.

The `lic` repo keeps a copy of `docs/` for compiler CI gates (Lean semantics, plan loops) until it is wired as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) of this repository. **Handbook and site edits belong here.**

## Layout

| Path | Purpose |
|------|---------|
| `docs/` | MkDocs source (handbook, guides, specs, release notes) |
| `mkdocs.yml` | Site navigation and theme |
| `scripts/build-docs.sh` | Local / CI build to `./site` |
| `.github/workflows/docs.yml` | Deploy GitHub Pages on `main` |

## License

Same as Li: GPL-3.0-or-later OR GPL-3.0-or-later.
