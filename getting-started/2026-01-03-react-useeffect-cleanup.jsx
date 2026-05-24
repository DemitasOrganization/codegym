// EXEMPLAR — not your history. Read-only reference shipped with the tool.
// kind: framework   |   track: react   |   difficulty: beginner
//
// This shows the FORMAT of a *framework* exercise — the kind that is NOT run.
// Correctness is judged against the RUBRIC at the bottom, not by execution.
// The skill takes difficulty from your config; this tag shows what beginner
// looks like for a framework track.
//
// ── TEACH BLOCK ────────────────────────────────────────────────────────────
// What: useEffect cleanup — the function you RETURN from an effect.
// Why:  Effects that subscribe to something (timers, listeners, sockets) must
//       undo that work, or you leak: duplicate intervals, stale listeners,
//       updates on unmounted components. The cleanup runs before the effect
//       re-runs and on unmount. Forgetting it is the single most common React
//       effect bug.
// How:  Return a function from the effect; React calls it to clean up:
//
//           useEffect(() => {
//             const id = setInterval(tick, 1000);
//             return () => clearInterval(id);   // <- cleanup
//           }, []);
//
// ── EXERCISE ───────────────────────────────────────────────────────────────
// ONE concept only — just the cleanup. Everything else is stubbed for you.
// Complete the effect in <Clock/> so it ticks every second AND clears the
// interval on unmount. Do not add state, props, styling, or anything else.

import { useState, useEffect } from "react";

function Clock() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    // TODO: start an interval that increments `seconds` every 1000ms,
    // and return a cleanup that stops it.
  }, []);

  return <div>{seconds}s</div>;
}

export default Clock;

// ── EVALUATION RUBRIC (fixed before you solve — do not edit) ────────────────
// Not executed. The skill judges the solution criterion by criterion and
// reports which are met / missed, showing the idiomatic form for any miss.
//
//  [ ] starts the interval inside the effect (not in render body)
//  [ ] updates state with the functional updater  setSeconds(s => s + 1)
//      (avoids the stale-closure bug on `seconds`)
//  [ ] RETURNS a cleanup function that calls clearInterval
//  [ ] dependency array is [] so the effect sets up once
//  [ ] does not introduce anything beyond the single taught concept
