---
name: codegym
description: >
  A daily ~15-minute coding drill. When the user invokes "codegym" (or
  /codegym), run the daily loop: read state, pick a track and concept, teach it
  briefly, set one bounded exercise, then evaluate the user's solution and
  record the result. Use whenever the user says "codegym", "daily drill",
  "morning exercise", or opens a repo containing codegym.config.md.
---

# Code Gym

A teach-then-test loop for keeping coding skills sharp in ~15 minutes a morning.
Each session teaches one concept, sets one exercise that tests exactly that
concept, evaluates the solution, and appends a single line to the ledger. State
lives in the repo, so every session behaves identically regardless of who runs
it or when.

The whole point is habit. A simple loop the user trusts and opens five mornings
a week beats a clever one they fight. Resist adding adaptive curves, dashboards,
or elaborate rubrics until the plain version has been run for a few weeks and
real friction tells you what to add.

---

## 1. On every invocation: detect, then route

Do not treat "is this initialized?" as a special case. Read state first; the
absence of state simply routes you to init. The presence of
`codegym.config.md` IS the initialized flag — there is no separate marker.

```
codegym invoked
  └─ does codegym.config.md exist?
        ├─ no  → FIRST RUN. Go to §2 (init).
        └─ yes → NORMAL MORNING. Go to §3 (daily loop).
```

Explicit sub-commands override the auto-route:

- `codegym init` — force the init path. If config already exists, this is a
  **reconfigure**: load it, let the user change/add tracks or difficulty, write
  it back. Never wipe history.
- `codegym reconfig` — alias for init-on-existing-config.

**Idempotency is mandatory.** Init must never overwrite an existing ledger,
existing solutions, or existing config without explicit confirmation. The rule
is *detect → confirm → write only what is missing*. Running init twice, or in a
half-set-up repo, must be safe.

---

## 2. Init (first run / reconfigure)

Init exists to capture **intent the repo cannot infer from its own contents**.
Folders and ledger entries tell you *history*; they can never tell you what the
user *wants*. So configuration is always written down explicitly, never
reconstructed from which folders happen to exist.

Interactively gather, then write `codegym.config.md` (schema in that file's
header). Collect:

1. **Tracks.** A track is one *thing to practice*. It is either:
   - a **language** (e.g. `python`, `c`, `javascript`, `typescript`), or
   - a **framework/library** (e.g. `react`, `fastapi`).
2. **Kind per track.** `runnable` or `framework` (see §4). Languages are
   normally `runnable`; frameworks are normally `framework`. The user may
   override.
3. **Difficulty per track.** `beginner` | `intermediate` | `advanced`, set
   independently for each track (the user is not equally strong everywhere).
4. **Rotation rule.** Default: weighted toward the track with the weakest
   recent scores, with a floor so no track goes stale longer than N days.
   Simpler alternative: strict round-robin.
5. **Scoring scale.** Default `1–5`. Keep it stable forever — the ledger's
   value is comparability across months. Do not redesign it later.

After confirming, scaffold only what is missing: one folder per track, an empty
`ledger.md`, an empty `weakspots.md`, and `codegym.config.md`. Optionally
generate the user's first exercise immediately so the first session ends in a
win.

Never scaffold history. A fresh user must start with an empty ledger and no
solutions. `getting-started/` ships with the tool and is read-only reference —
it is **never** treated as the user's history (see §6).

---

## 3. The daily loop (normal morning)

1. **Read state.** `codegym.config.md` (intent), `ledger.md` (history),
   `weakspots.md` (recurring misses). Scan track folders to know what concepts
   have been covered. **Exclude `getting-started/` from all history scans.**
2. **Select a track.** Apply the rotation rule from config. Bias toward weak
   tracks; honor the staleness floor.
3. **Select a concept.** Within the track, prefer:
   - concepts in `weakspots.md` (spaced re-surfacing of things flubbed), then
   - concepts not recently drilled,
   - never the exact concept from the last session in that track.
4. **Generate the exercise** per the contract in §4. Write it as a file in the
   track folder, named `YYYY-MM-DD-<concept-slug>.<ext>`. The file contains, in
   order: the teach block, the exercise prompt, a stub, and — committed up front
   — the evaluation criteria (test cases for `runnable`, rubric for
   `framework`).
5. **Hand off.** Tell the user the file is ready and to solve it, then say
   "done".
6. **Evaluate** per §5 when the user returns. Settle correctness by the
   kind-appropriate method. Give feedback on the *interesting* layer: idiom,
   the cleaner construct, the missed edge, complexity — not just pass/fail.
7. **Record.** Append one line to `ledger.md` (format in that file). Update
   `weakspots.md` if a recurring miss is confirmed or a resolved one clears.
8. **Commit & push.** `git add`, `git commit -m "codegym: <date> <track>
   <concept> (<score>)"`, `git push`. This closes the loop with no manual
   round-trip.

---

## 4. The generation contract

Every generated exercise MUST obey all of the following.

### 4.1 Structure (both kinds, in this order)

1. **Teach block** — what we're learning, why it matters, how it's done.
2. **Exercise** — tests exactly the concept just taught.
3. **Stub** — the starting point the user fills in.
4. **Evaluation criteria** — fixed *before* the user solves, never invented
   afterward to match their answer. Test cases (runnable) or rubric (framework).

### 4.2 The teach block

- Brief: one short paragraph, roughly 3–6 sentences total across what / why / how.
- The **"how" is load-bearing** and must include at least one tiny inline
  illustration of the construct or pattern — a one-liner showing its *form* —
  separate from the exercise. The user must see the shape before being asked to
  produce it. Do not let "how" decay into more prose about the concept.
- Reading time counts against the 15-minute box. Long teach block → shorter
  exercise.

### 4.3 Test what you taught (the coupling that keeps the loop honest)

- The exercise tests the concept the teach block just explained — and nothing
  materially beyond it.
- Any *other* construct the exercise requires must be one the user already has,
  knowable from the ledger. Never test unseen material.

### 4.4 One concept only — and the time box

- Isolate a single concept. Stub everything else.
- This is **most fragile for `framework` exercises**, which sprawl instantly
  ("build a React component" → state + props + effects + styling). Hard rule:
  a framework exercise targets exactly one thing (just `useEffect` cleanup;
  just a FastAPI dependency) and stubs the rest. If it can't be taught-and-
  tested in ~15 minutes, it's too big — narrow the concept.

### 4.5 The two kinds

- **`runnable`** — self-contained code (syntax/idiom drills). Correctness is
  **objective**, settled by execution against the test cases. The "how"
  illustration shows a language construct.
- **`framework`** — usage of a library/framework where running it in a morning
  drill is impractical and unnecessary. Correctness is a **judgment** against a
  **rubric**, not execution. The "how" illustration shows the framework pattern
  (a minimal route, a minimal component).

  The rubric replaces test cases as the structural equivalent and is generated
  *with the exercise*. It lists concrete, checkable criteria, e.g. for a
  FastAPI body-handling drill: *uses a Pydantic model for the body; correct
  path-vs-query param distinction; returns the right status code; dependency
  injected, not instantiated in-handler.* Evaluation is "did the solution hit
  these criteria" — reviewable and consistent across months, not vibes.

The kind is fixed at generation time and the teach block, exercise shape, and
evaluation method must all agree with it. A framework exercise graded as if
runnable (or vice versa) is the failure mode.

### 4.6 Difficulty modulates BOTH halves

Difficulty (from config, per track) dials two things, not one: how much the
teach block hands you, *and* how hard the exercise is. State both per level:

| Level | Teach block ("how") | Exercise | Edges |
|---|---|---|---|
| **beginner** | shows the construct almost fully | complete / adapt the shown construct | trivial |
| **intermediate** | shows the shape once | produce it in a new context | one real edge |
| **advanced** | terse reminder ("you know closures; here's the IIFE pattern") | idiomatic production under complexity pressure | nasty edges, complexity matters |

Getting this backwards (easy exercise + terse explanation, or hard exercise +
spoon-fed explanation) is wrong. Beginner = generous teaching *and* easy
exercise; advanced = terse teaching *and* hard exercise.

---

## 5. Evaluation

- **runnable:** execute the solution against the committed test cases (python,
  node/tsc, gcc are available). Correctness is decided by the run, not by
  reading. Then comment on idiom, a cleaner construct, the edge they missed,
  complexity.
- **framework:** assess against the committed rubric, criterion by criterion.
  Be explicit that this is judgment, not execution — say which criteria were
  met, which were missed, and show the idiomatic form for any miss.
- **Score** on the configured scale. Be consistent run-to-run; the ledger is
  only useful if a 3 means the same thing in June as in March.
- **Feedback is the product.** A single day's grade is cheap; the longitudinal
  view is the value. When the ledger shows a pattern ("edge cases missed on
  three of the last five"), say so — that's what changes behavior.

---

## 6. State model (what's truth, what's history, what ships)

| File / dir | Role | Written by | Read for |
|---|---|---|---|
| `codegym.config.md` | **intent / source of truth** | init only | routing, difficulty, kinds |
| `ledger.md` | history (one line/day) | every session | selection, longitudinal feedback |
| `weakspots.md` | recurring misses | every session | biasing selection |
| `<track>/*.<ext>` | the user's solutions = a growing cookbook | every session | "what's been covered" |
| `getting-started/` | **read-only exemplars that ship with the tool** | tool authors | format/teaching reference only |
| `README.md` | human onboarding | tool authors | — |

Rules that follow:

- Config is **never** inferred from artifacts. If folders imply something config
  doesn't say, config wins (a user who hasn't done a C drill yet has no `c/`
  files — that must not drop C from rotation).
- `getting-started/` is **never** rotation history. Exclude it from every scan
  that asks "what has the user done." Otherwise every fresh user looks like they
  already completed a C pointer drill.
- What ships: skill + README + `getting-started/` + an example config. What does
  NOT ship: a populated ledger, weakspots, or anyone's solutions. `.gitignore`
  and init must agree on this split.
