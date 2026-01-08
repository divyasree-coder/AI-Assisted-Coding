# Reverse an array

# Get user input for the array (space-separated numbers)
input_str = input("Enter the array elements separated by spaces: ")

# Split the input string into a list of strings, then convert to floats
arr = [float(x) for x in input_str.split()]

# Reverse the array
arr.reverse()

# Output the reversed array
print("Reversed array:", arr)