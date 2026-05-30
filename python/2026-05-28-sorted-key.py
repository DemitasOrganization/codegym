"""
CODE GYM — 2026-05-28 — python — sorted-key (beginner, runnable)
================================================================

TEACH
-----
WHAT: `sorted(iterable, key=...)` returns a new sorted list, where `key` is a
function applied to each item to decide *what to sort by* (the items themselves
are returned unchanged). WHY: it lets you sort by a derived property — length,
lowercased text, a tuple field — without hand-rolling a comparison or mutating
the original. HOW: pass any one-argument function as `key`; Python calls it on
each element and sorts by the results. `reverse=True` flips the order.

    sorted([-3, 1, -2], key=abs)          # [1, -2, -3]   (sorted by |x|)
    sorted(["Bob", "al", "CY"], key=len)  # ['al', 'CY', 'Bob']

A handy one: `key=str.lower` sorts text case-insensitively without changing it.


EXERCISE
--------
Write `sort_ci(words)` that returns a NEW list with the words sorted
alphabetically, ignoring case (so "Apple" and "apple" sort together, and a
capital letter does not jump ahead of a lowercase one). The original casing of
each word must be preserved in the output, and the input list must not be
mutated.

    sort_ci(["banana", "Apple", "cherry"]) -> ["Apple", "banana", "cherry"]

Use `sorted` with a `key=`. Do not lowercase the actual words in the result,
and do not sort in place with `.sort()`.
"""

def sort_ci(words):
    return sorted(words, key=str.lower)



# ============================================================
# EVALUATION CRITERIA — committed before solving. Do not edit.
# Run this file: `python3 2026-05-28-sorted-key.py`
# ============================================================
if __name__ == "__main__":
    tests = [
        (["banana", "Apple", "cherry"],   ["Apple", "banana", "cherry"]),
        (["Zoo", "ant", "Bee"],           ["ant", "Bee", "Zoo"]),       # case-insensitive ordering
        (["solo"],                        ["solo"]),
        ([],                              []),                          # empty
        (["b", "B", "a", "A"],            ["a", "A", "b", "B"]),        # stable within equal keys
    ]
    passed = 0
    for words, expected in tests:
        original = list(words)
        got = sort_ci(words)
        ok = got == expected
        mutated = words != original
        passed += ok and not mutated
        flag = "PASS" if (ok and not mutated) else "FAIL"
        note = "" if ok else f"   expected {expected!r}"
        note += "   (MUTATED INPUT!)" if mutated else ""
        print(f"{flag}  sort_ci({original!r}) -> {got!r}{note}")
    print(f"\n{passed}/{len(tests)} passed")
