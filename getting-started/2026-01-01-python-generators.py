# EXEMPLAR — not your history. Read-only reference shipped with the tool.
# kind: runnable   |   track: python   |   difficulty: intermediate
#
# This file shows the FORMAT of a codegym exercise. The skill matches this
# shape; it takes DIFFICULTY from your config, not from this tag. The tag here
# only tells you "this is what intermediate looks like."
#
# ── TEACH BLOCK ───────────────────────────────────────────────────────────
# What: A generator yields values lazily instead of building a list in memory.
# Why:  It's the idiomatic Python way to stream/transform sequences without
#       materializing them — lower memory, composable, and it's what most
#       stdlib iteration tools expect. Reaching for a list is the common tell
#       of non-idiomatic Python.
# How:  Use `yield` in a function; each call to next() runs to the next yield:
#
#           def squares(n):
#               for i in range(n):
#                   yield i * i        # <- yields one value, then pauses
#
#       `squares(3)` produces 0, 1, 4 lazily — nothing is stored.
#
# ── EXERCISE ──────────────────────────────────────────────────────────────
# Write `running_max(nums)` as a GENERATOR that yields the running maximum
# seen so far. It must not build or return a list. (intermediate edge: it must
# handle an empty input by yielding nothing, not erroring.)
#
#   running_max([3, 1, 4, 1, 5])  ->  yields 3, 3, 4, 4, 5
#   running_max([])               ->  yields nothing

def running_max(nums):
    # your solution here
    ...


# ── EVALUATION CRITERIA (fixed before you solve — do not edit) ──────────────
# These run as-is. Correctness is settled by execution.
if __name__ == "__main__":
    import types
    g = running_max([3, 1, 4, 1, 5])
    assert isinstance(g, types.GeneratorType), "must be a generator, not a list"
    assert list(g) == [3, 3, 4, 4, 5]
    assert list(running_max([])) == []
    assert list(running_max([7])) == [7]
    print("PASS")
