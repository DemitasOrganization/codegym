# kind: runnable   |   track: python   |   difficulty: beginner
#
# ── TEACH BLOCK ───────────────────────────────────────────────────────────
# What: A list comprehension builds a list in one expression by looping over an
#       iterable, optionally filtering.
# Why:  It's the idiomatic Python way to transform/filter a sequence — clearer
#       and tighter than an empty list + append loop, which is the usual tell of
#       non-idiomatic Python.
# How:  The form is  [ <expr> for <var> in <iterable> if <condition> ]
#       The `if` is optional. For example:
#
#           [n * 2 for n in [1, 2, 3]]            ->  [2, 4, 6]
#           [n for n in [1, 2, 3, 4] if n % 2]    ->  [1, 3]   (odds only)
#
# ── EXERCISE ──────────────────────────────────────────────────────────────
# Write `even_squares(nums)` that returns a list of the SQUARES of only the
# even numbers in `nums`, in order. Use a single list comprehension (no append
# loop). Trivial edge: an empty input returns an empty list.
#
#   even_squares([1, 2, 3, 4])  ->  [4, 16]
#   even_squares([])            ->  []

def even_squares(nums):
    return [n*n for n in nums if n%2 == 0]


# ── EVALUATION CRITERIA (fixed before you solve — do not edit) ──────────────
# These run as-is. Correctness is settled by execution.
if __name__ == "__main__":
    assert even_squares([1, 2, 3, 4]) == [4, 16]
    assert even_squares([]) == []
    assert even_squares([2, 4, 6]) == [4, 16, 36]
    assert even_squares([1, 3, 5]) == []
    assert even_squares([0, -2, 5]) == [0, 4]
    print("PASS")
