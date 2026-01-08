# Prime Number Checker Documentation

Hey! So, this is all about two ways to check if a number is prime in Python. One keeps it all in the main code, the other uses a function. A prime number? It's bigger than 1 and only divisible by 1 and itself – no other factors sneaking in. Both ask for your input and spit out the answer.

## Version 1: No Function, Just Straight Code
This one's all about doing the check right there in the main script, no extra functions needed.

Think of it like this:
- Asks for a number and turns it into an integer.
- Starts with a flag saying "yeah, probably prime" (True).
- If it's 1 or less, nope, not prime.
- Otherwise, loops from 2 up to the square root, checking if it divides evenly. If yes, flag to False and stop.
- Then tells you the result.

Simple, direct, everything in one place.

## Version 2: With a Handy Function
Here, we tuck the checking into a function called `is_prime`, making it reusable.

- The function takes the number, does the checks, and returns True or False.
- Same logic as Version 1, but wrapped up.
- Main code just calls the function and prints.

Super useful if you need to check primes multiple times.

Both are tweaked for speed: quick outs for small or even numbers, only check up to sqrt. Runs in O(sqrt n) time.

To try it, save as a .py file, run with Python, enter a number, see what happens.

Like, put in 7: "7 is a prime number." Put in 4: "4 is not a prime number."

It handles edge cases like 1 or negatives fine, no extra libraries required.