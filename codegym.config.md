# codegym.config.md

**This file is the source of truth for intent.** Its presence means the repo is
initialized. It is written at init (or reconfigure) and read at the start of
every session. It is never inferred from which folders or files exist — folders
are history, this is intent. If the two ever disagree, this file wins.

Run `codegym reconfig` to change it (adds/edits tracks or difficulty; never
wipes history).

---

## Tracks

| track | kind | difficulty |
|---|---|---|
| python | runnable | beginner |

Notes:
- `kind` is `runnable` (correctness settled by execution) or `framework`
  (correctness judged against a rubric, not run). See SKILL §4.5.
- Difficulty is per track and is one of `beginner | intermediate | advanced`.

## Rotation

```
rule: weighted-weakest      # or: round-robin
staleness_floor_days: 4     # no track goes untouched longer than this
```

## Scoring

```
scale: 1-5                  # keep stable forever; comparability is the point
```

---

## Difficulty definitions (what the levels actually mean)

- **beginner** — Teach block shows the construct almost fully. Exercise:
  complete or lightly adapt the shown construct. Edges: trivial.
- **intermediate** — Teach block shows the shape once. Exercise: produce it in
  a new context. Edges: one real edge case.
- **advanced** — Teach block is a terse reminder. Exercise: idiomatic
  production under complexity pressure, no hand-holding. Edges: nasty;
  complexity matters.
