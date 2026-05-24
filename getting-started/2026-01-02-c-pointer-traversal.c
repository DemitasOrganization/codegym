/* EXEMPLAR — not your history. Read-only reference shipped with the tool.
 * kind: runnable   |   track: c   |   difficulty: beginner
 *
 * Shows the FORMAT of a codegym C exercise. The skill takes DIFFICULTY from
 * your config; this tag only shows "this is what beginner looks like." C is
 * the track where a worked example helps most, so the teach block holds your
 * hand more here.
 *
 * ── TEACH BLOCK ──────────────────────────────────────────────────────────
 * What: Walking a string with a pointer instead of an index.
 * Why:  Pointer traversal is the C idiom — it's how the standard library is
 *       written, and understanding it is the gateway to everything else in C
 *       memory handling. The NUL terminator '\0' is what marks the end; there
 *       is no length stored alongside the string.
 * How:  Advance a char* until you hit the terminator:
 *
 *           char *p = str;
 *           while (*p != '\0') {   // <- *p reads the char p points at
 *               p++;               // <- move the pointer one char forward
 *           }
 *
 *       At the end, p points AT the '\0'. (beginner: the construct above is
 *       almost the whole answer — you adapt it.)
 *
 * ── EXERCISE ─────────────────────────────────────────────────────────────
 * Implement `size_t str_len(const char *s)` that returns the number of
 * characters before the NUL terminator, using POINTER traversal (no array
 * indexing, no library strlen). Beginner edge: the empty string "" returns 0.
 *
 *   str_len("hi")  -> 2
 *   str_len("")    -> 0
 */

#include <stddef.h>
#include <assert.h>
#include <stdio.h>

size_t str_len(const char *s) {
    /* your solution here */
    return 0;
}

/* ── EVALUATION CRITERIA (fixed before you solve — do not edit) ───────────
 * Compiled and run as-is. Correctness is settled by execution. */
int main(void) {
    assert(str_len("hi") == 2);
    assert(str_len("") == 0);
    assert(str_len("pointer") == 7);
    printf("PASS\n");
    return 0;
}
