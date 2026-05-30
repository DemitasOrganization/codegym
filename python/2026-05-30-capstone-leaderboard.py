"""
CODE GYM — 2026-05-30 — python — capstone-leaderboard (beginner+, runnable)
===========================================================================

A CAPSTONE, not a single-concept drill. The point is to *combine* the four
things you've drilled into one small helper that does something real:

    zip                 -> pair each name with its score
    sorted(key=...)     -> rank them (and break ties cleanly)
    enumerate           -> number the ranks 1, 2, 3, ...
    list comprehension  -> build the formatted output rows

This is the kind of 10-line helper you'd actually paste into a script to print
a leaderboard from two columns of data.


EXERCISE
--------
Write `leaderboard(names, scores, top=None)`.

`names` and `scores` are two PARALLEL lists (names[i] scored scores[i]).
Return a list of formatted strings, highest score first:

    "1. Bob — 95"          (rank, a period, the name, a space-em-dash-space, score)

Rules:
  - Pair each name with its score using zip.
  - Rank by score, HIGHEST first.
  - Break ties alphabetically by name, CASE-INSENSITIVELY (so "Alice" and
    "alice" sort together and a capital doesn't jump ahead).
  - Number ranks starting at 1.
  - If `top` is given (an int), return only the first `top` rows; if it's
    None, return all rows.
  - The separator between name and score is " — " (space, em dash U+2014, space).
    You can copy it straight from the expected output below.
  - Do not mutate the input lists.

Try to lean on the four constructs above rather than hand-rolled loops. A clean
solution is roughly 3–5 lines of body.

    leaderboard(["Alice", "Bob", "Cara"], [90, 95, 88])
    # -> ["1. Bob — 95", "2. Alice — 90", "3. Cara — 88"]
"""


def leaderboard(names, scores, top=None):
    ranked = sorted(zip(names, scores), key=lambda p: (-p[1], p[0].lower()))
    rows = [f"{i}. {name} — {score}" for i, (name, score) in enumerate(ranked, start=1)]
    return rows[:top]


# ============================================================
# EVALUATION CRITERIA — committed before solving. Do not edit.
# Run this file: `python3 2026-05-30-capstone-leaderboard.py`
# ============================================================
if __name__ == "__main__":
    tests = [
        # (names, scores, top, expected)
        (
            ["Alice", "Bob", "Cara"],
            [90, 95, 88],
            None,
            ["1. Bob — 95", "2. Alice — 90", "3. Cara — 88"],
        ),
        # tie on score -> alphabetical, case-insensitive ("Alice" before "bob")
        (["bob", "Alice"], [70, 70], None, ["1. Alice — 70", "2. bob — 70"]),
        # top truncation keeps the highest `top` rows
        (["A", "B", "C", "D"], [1, 4, 3, 2], 2, ["1. B — 4", "2. C — 3"]),
        # case-insensitive tie-break, mixed casing, three-way tie
        (
            ["zoe", "Zane", "ABE"],
            [50, 50, 50],
            None,
            ["1. ABE — 50", "2. Zane — 50", "3. zoe — 50"],
        ),
        # empty
        ([], [], None, []),
        # single
        (["Solo"], [42], None, ["1. Solo — 42"]),
    ]

    passed = 0
    for names, scores, top, expected in tests:
        n_orig, s_orig = list(names), list(scores)
        got = leaderboard(names, scores, top)
        ok = got == expected
        mutated = names != n_orig or scores != s_orig
        passed += ok and not mutated
        flag = "PASS" if (ok and not mutated) else "FAIL"
        extra = (
            "" if ok else f"\n        expected {expected!r}\n        got      {got!r}"
        )
        extra += "   (MUTATED INPUT!)" if mutated else ""
        print(f"{flag}  leaderboard({names!r}, {scores!r}, top={top!r}){extra}")
    print(f"\n{passed}/{len(tests)} passed")
