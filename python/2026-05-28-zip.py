"""
CODE GYM — 2026-05-28 — python — zip (beginner, runnable)
=========================================================

TEACH
-----
WHAT: `zip` walks two (or more) iterables in lockstep, handing you one item
from each on every step. WHY: it replaces indexing two lists by a shared
counter (`a[i]`, `b[i]`) with a loop that reads cleanly and can't fall out of
sync. HOW: pass the iterables to `zip(...)` and unpack the pair in the
for-target. One gotcha worth knowing: `zip` stops at the SHORTEST input, so
extra items in the longer one are simply dropped.

    for name, age in zip(["ann", "bo"], [30, 25]):
        print(name, age)          # ann 30 / bo 25

    list(zip([1, 2, 3], ["a", "b"]))   # [(1, 'a'), (2, 'b')]  -> 3 dropped


EXERCISE
--------
Write `combine(names, scores)` that takes a list of names and a list of integer
scores and returns a list of strings of the form "<name>: <score>", pairing
them by position.

    combine(["ann", "bo"], [90, 75]) -> ["ann: 90", "bo: 75"]

Use `zip` to walk the two lists together — do not index by `range(len(...))`
or a manual counter. (Lean on zip's stop-at-shortest behavior for the
mismatched-length case; you should not need to special-case it.)
"""


def combine(names, scores):
    return [f"{name}: {score}" for name, score in zip(names,scores)]



# ============================================================
# EVALUATION CRITERIA — committed before solving. Do not edit.
# Run this file: `python3 2026-05-28-zip.py`
# ============================================================
if __name__ == "__main__":
    tests = [
        (["ann", "bo"], [90, 75],        ["ann: 90", "bo: 75"]),
        (["solo"],      [100],           ["solo: 100"]),
        ([],            [],              []),                     # both empty
        (["a", "b"],    [1],             ["a: 1"]),               # scores shorter -> drop "b"
        (["x"],         [5, 6, 7],       ["x: 5"]),               # names shorter -> drop extras
    ]
    passed = 0
    for names, scores, expected in tests:
        got = combine(names, scores)
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  combine({names!r}, {scores!r}) -> {got!r}"
              + ("" if ok else f"   expected {expected!r}"))
    print(f"\n{passed}/{len(tests)} passed")
