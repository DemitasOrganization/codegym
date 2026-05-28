"""
CODE GYM — 2026-05-25 — python — enumerate (beginner, runnable)
================================================================

TEACH
-----
WHAT: `enumerate` pairs each item of an iterable with its index, so you loop
over both at once. WHY: it replaces the clunky `for i in range(len(seq))`
(then indexing `seq[i]` by hand) with something that reads like English and
can't go out of sync with the list. HOW: wrap the iterable in `enumerate(...)`
and unpack two names in the for-target; pass `start=` to choose the first index.

    for i, item in enumerate(["a", "b", "c"]):
        print(i, item)        # 0 a / 1 b / 2 c

    for n, item in enumerate(["a", "b"], start=1):
        print(n, item)        # 1 a / 2 b


EXERCISE
--------
Write `number_lines(lines)` that takes a list of strings and returns a list of
strings where each line is prefixed with its 1-based line number, a period, and
a space.

    number_lines(["alpha", "beta"]) -> ["1. alpha", "2. beta"]

Use `enumerate` (with the `start=` argument) — do not use range(len(...)) or a
manual counter.
"""


def number_lines(lines):
    return [f"{i}. {line}" for i, line in enumerate(lines, start=1)]



# ============================================================
# EVALUATION CRITERIA — committed before solving. Do not edit.
# Run this file: `python3 2026-05-25-enumerate.py`
# ============================================================
if __name__ == "__main__":
    tests = [
        (["alpha", "beta"],            ["1. alpha", "2. beta"]),
        (["only"],                     ["1. only"]),
        ([],                           []),                       # empty input
        (["", "x"],                    ["1. ", "2. x"]),          # empty string line
        (["a", "b", "c", "d"],         ["1. a", "2. b", "3. c", "4. d"]),
    ]
    passed = 0
    for args, expected in tests:
        got = number_lines(args)
        ok = got == expected
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  number_lines({args!r}) -> {got!r}"
              + ("" if ok else f"   expected {expected!r}"))
    print(f"\n{passed}/{len(tests)} passed")
