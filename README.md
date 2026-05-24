# Code Gym

A daily ~15-minute coding drill that runs inside [Claude Code](https://docs.claude.com/en/docs/claude-code).
Each morning it teaches you one concept, sets one small exercise that tests
exactly that concept, evaluates your solution, and records the result — then
commits and pushes. State lives in this repo, so it picks up exactly where you
left off.

It practices two things:

- **Languages** (`python`, `c`, `typescript`, …) — *runnable* drills, graded by
  actually executing your code against test cases.
- **Frameworks/libraries** (`react`, `fastapi`, …) — *framework* drills, graded
  by judgment against a rubric (no need to run a whole app in a morning).

Every exercise follows a **teach-then-test** shape: a short paragraph on *what*
you're learning, *why* it matters, and *how* it's done (with a tiny inline
example), then an exercise that tests that one thing.

## Quick start

1. Clone this repo and open it in Claude Code.
2. Run `codegym`. On a fresh repo it will set you up: pick your tracks
   (languages and/or frameworks), choose a difficulty **per track**, and a
   rotation rule. This writes `codegym.config.md`.
3. From then on, just run `codegym` each morning. It reads your state, picks
   today's track and concept, and writes the exercise into a track folder.
4. Solve it in your editor, say "done", and it evaluates, scores, logs one line
   to `ledger.md`, and commits + pushes.

Re-run `codegym init` (or `codegym reconfig`) anytime to add a track or change
difficulty. It won't wipe your history.

## What's in here

| Path | What it is |
|---|---|
| `.claude/skills/codegym/SKILL.md` | the skill — all the logic |
| `codegym.config.example.md` | example config; `init` writes your real one |
| `ledger.md` | one line per day (your history) — ships empty |
| `weakspots.md` | recurring misses, biases what you get — ships empty |
| `getting-started/` | three read-only exemplars showing the format |
| `<track>/` | created by `init` for each track you choose; your solutions accumulate there as a personal cookbook |

The three files in `getting-started/` show the exact format of an exercise —
one runnable (Python), one runnable + low-level (C pointers), one framework
(React, rubric-graded). They are **reference only**: Code Gym never counts them
as your history, and they set *format*, not difficulty — difficulty always
comes from your config.

## Design notes

- **Config is intent; folders are history.** What you want (tracks, difficulty)
  is written in `codegym.config.md` and never guessed from which folders exist.
- **Difficulty modulates teaching and exercise together.** Beginner = generous
  teaching + easy exercise; advanced = terse reminder + hard exercise.
- **Keep it simple on purpose.** No adaptive curves or dashboards at first. The
  thing that makes this work is opening it five mornings a week.

## Contributing

PRs that add `getting-started/` exemplars for more tracks are welcome — they set
the format and teaching quality for everyone, so keep them tight: one concept,
a real teach block with an inline "how", and fixed evaluation criteria
(test cases for runnable, a rubric for framework).
