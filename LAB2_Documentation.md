# LAB2.PY Documentation: Fibonacci Generators

Yo! Dive into this script that whips up Fibonacci strings in two wild styles: looping it up (iteration) and calling back on itself (recursion). Fibonacci? That sequence where each step is the sum of the last two, kicking off with 0 and 1 – think 0, 1, 1, 2, 3, 8, 13...

## Iterative Method
The loop master – builds the chain link by link, no recursion headaches.

Asks for term count, then:
- Zero or negative? Blank slate.
- Just one? "0" it is.
- More? Kicks off with [0, 1], loops to add sums.
- Strings 'em up with spaces.

Lightning fast, scales like a dream.

## Recursive Method
The self-calling wizard, boosted with memory tricks to not repeat itself.

`fib_recursive` with `@lru_cache` – remembers what it figured out, so no wasted brainpower.

Same drill: input terms, output string.

Cache makes recursion a rocket, not a slog.

## How to Roll
Launch the script, drop in term numbers twice, watch the magic.

Say 5: "Fibonacci string: 0 1 1 2 3" pops up for both.

Iterative wins speed races for huge numbers; recursive shines with smart caching but nibbles memory. Both ace edge cases like zilch or negatives.