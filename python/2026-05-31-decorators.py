# codegym — python / decorators (beginner, runnable)
# 2026-05-31
#
# ── TEACH ──────────────────────────────────────────────────────────────────
# WHAT: A decorator is a function that takes a function and returns a new
#   function wrapping it. `@deco` above a def is just sugar for
#   `handler = deco(handler)`. This is the entire mechanism behind FastAPI's
#   `@app.get("/")` — the framework wraps your handler to register and call it.
#
# WHY: In web code you constantly want to add behavior *around* a handler
#   without editing the handler itself: timing, auth checks, logging, call
#   counting, caching. Decorators are how you bolt that on cleanly. If you can
#   write one by hand, FastAPI's routing/dependency magic stops being magic.
#
# HOW: The wrapper must forward *args/**kwargs so it works on any handler,
#   return the wrapped function's result, and use functools.wraps so the
#   wrapped function keeps its real __name__ (frameworks introspect that).
#   The shape:
#
#       import functools
#       def log_calls(fn):
#           @functools.wraps(fn)
#           def wrapper(*args, **kwargs):
#               result = fn(*args, **kwargs)   # forward args, capture result
#               wrapper.calls += 1             # state lives on the wrapper
#               return result                  # MUST return it
#           wrapper.calls = 0
#           return wrapper
#
# ── EXERCISE ───────────────────────────────────────────────────────────────
# Write a decorator `track_calls` that wraps any handler so that:
#   1. Calling the wrapped function returns the original's return value,
#      unchanged.
#   2. It forwards ALL positional and keyword arguments to the original.
#   3. The wrapped function exposes a `.calls` attribute (int) that counts how
#      many times it has been invoked, starting at 0.
#   4. The wrapped function keeps the original's __name__ (use functools.wraps).
#
# Stub everything but the decorator itself.

import functools


def track_calls(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        wrapper.calls += 1
        return result
    wrapper.calls = 0
    return wrapper


# ── EVALUATION CRITERIA (committed before solving — do not edit) ─────────────
# Run this file. All asserts must pass and it must print "OK".

if __name__ == "__main__":
    @track_calls
    def add(a, b):
        """Add two numbers."""
        return a + b

    @track_calls
    def greet(name, *, greeting="Hello"):
        return f"{greeting}, {name}!"

    # 1 & 2: return value + positional/keyword arg forwarding
    assert add(2, 3) == 5
    assert add(b=4, a=1) == 5
    assert greet("Ada") == "Hello, Ada!"
    assert greet("Ada", greeting="Hi") == "Hi, Ada!"

    # 3: per-function call counter, independent across decorated functions
    assert add.calls == 2, f"expected 2, got {add.calls}"
    assert greet.calls == 2, f"expected 2, got {greet.calls}"

    # 4: identity preserved for framework introspection
    assert add.__name__ == "add", f"name not preserved: {add.__name__!r}"
    assert add.__doc__ == "Add two numbers."

    print("OK")
