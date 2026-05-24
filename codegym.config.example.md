# codegym.config.md

**This file is the source of truth for intent.** Its presence means the repo is
initialized. It is written at init (or reconfigure) and read at the start of
every session. It is never inferred from which folders or files exist — folders
are history, this is intent. If the two ever disagree, this file wins.

The version below is a filled-in *example*. `init` produces one of these from
your answers. Edit it by hand or run `codegym reconfig` to change it.

---

## Tracks

A **track** is one thing you're practicing. It is either a **language**
(runnable) or a **framework/library** (framework). Each track carries its own
kind and its own difficulty — you are not equally strong everywhere.

| track | kind | difficulty |
|---|---|---|
| python | runnable | intermediate |
| c | runnable | beginner |
| typescript | runnable | intermediate |
| react | framework | beginner |
| fastapi | framework | beginner |

Notes:
- `kind` is `runnable` (correctness settled by execution) or `framework`
  (correctness judged against a rubric, not run). See SKILL §4.5.
- JS/TS are the substrate that React/FastAPI-adjacent tracks build on; you can
  list `javascript` and `typescript` as their own tracks *and* have framework
  tracks that assume them.
- Difficulty is per track and is one of `beginner | intermediate | advanced`.

## Rotation

```
rule: weighted-weakest      # or: round-robin
staleness_floor_days: 4     # no track goes untouched longer than this
```

`weighted-weakest` biases selection toward the track with the weakest recent
ledger scores, while the floor guarantees variety. `round-robin` is the simple
deterministic alternative.

## Scoring

```
scale: 1-5                  # keep stable forever; comparability is the point
```

Do not redesign the scale later — a 3 in June must mean what a 3 meant in March,
or the longitudinal view is worthless.

---

## Difficulty definitions (what the levels actually mean)

The generator cannot act on a bare label. These concrete definitions drive
generation; the label is just shorthand. Difficulty modulates **both** the
teach block and the exercise (SKILL §4.6).

- **beginner** — Teach block shows the construct almost fully. Exercise:
  complete or lightly adapt the shown construct. Edges: trivial.
- **intermediate** — Teach block shows the shape once. Exercise: produce it in
  a new context. Edges: one real edge case.
- **advanced** — Teach block is a terse reminder. Exercise: idiomatic
  production under complexity pressure, no hand-holding. Edges: nasty;
  complexity matters.

These apply per track, so `python: advanced` and `c: beginner` coexist and mean
different things on the same morning.
