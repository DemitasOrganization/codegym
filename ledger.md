# Ledger

One line per session. This is the longitudinal record — the part read every
morning to route selection and to surface patterns over weeks. It stays tiny
forever because it logs *one takeaway*, not full problems (those live as files
in the track folders).

Format:

```
| date | track | concept | difficulty | kind | score | takeaway |
```

- **date** — YYYY-MM-DD
- **track** — must match a track in codegym.config.md
- **concept** — the single thing drilled (slug, matches the solution filename)
- **difficulty** — level used for this exercise
- **kind** — runnable | framework
- **score** — on the configured scale
- **takeaway** — one short note. This is the load-bearing field: it's what
  feeds weakspots and what makes "you've missed edges 3 of the last 5" possible.

This file ships **empty**. A fresh user starts with no history. The commented
rows below are illustrative and are never read as history.

| date | track | concept | difficulty | kind | score | takeaway |
|------|-------|---------|------------|------|-------|----------|
<!-- 2026-05-24 | python | generators | intermediate | runnable | 4 | clean, but reached for a list where a generator was the point |
<!-- 2026-05-25 | c      | pointer-arithmetic | beginner | runnable | 3 | off-by-one on the terminator; forgot the NUL byte |
<!-- 2026-05-26 | react  | useEffect-cleanup | beginner | framework | 5 | nailed the cleanup return; rubric fully met -->
