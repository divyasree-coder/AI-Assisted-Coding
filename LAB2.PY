# Hey, let's generate some Fibonacci sequences as strings!
# First, the iterative way – building it step by step with a loop.

# Ask the user how many terms they want
n = int(input("Enter the number of Fibonacci terms: "))

# Handle the easy cases first
if n <= 0:
    fib_str = ""  # Nothing to show
elif n == 1:
    fib_str = "0"  # Just the first one
else:
    # Start with the basics
    fib_list = [0, 1]
    # Add more terms by summing the last two
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    # Turn the list into a nice string
    fib_str = " ".join(map(str, fib_list[:n]))

# Show the result
print(f"Fibonacci string: {fib_str}")

# Now, the recursive way with a memory boost to make it fast.

# Import the caching tool
from functools import lru_cache

# Define the function with caching – it remembers results!
@lru_cache(maxsize=None)
def fib_recursive(k):
    if k <= 1:
        return k  # Base cases: 0 or 1
    return fib_recursive(k-1) + fib_recursive(k-2)  # Recursive sum

# Get another input for the recursive version
n2 = int(input("Enter the number of Fibonacci terms (recursive): "))

# Build the list using the function
if n2 <= 0:
    fib_str2 = ""  # Empty for no terms
else:
    fib_list2 = [fib_recursive(i) for i in range(n2)]
    fib_str2 = " ".join(map(str, fib_list2))  # String it up

# Print it out
print(f"Fibonacci string (recursive): {fib_str2}")
     # optimize the above code
# Optimized prime number checker without functions
num = int(input("Enter a number to check if it's prime: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
        # prime number checker with functions
# Prime number checker with functions
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    