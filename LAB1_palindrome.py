# Palindrome check

# Get user input for the string
string = input("Enter a string to check if it's a palindrome: ")

# Clean the string: convert to lowercase and remove spaces
cleaned = string.lower().replace(" ", "")

# Check if the cleaned string is equal to its reverse
is_palindrome = cleaned == cleaned[::-1]

# Output the result
if is_palindrome:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")