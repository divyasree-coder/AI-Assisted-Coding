# Remove duplicates from array

# Get user input for the array (space-separated numbers)
input_str = input("Enter the array elements separated by spaces: ")

# Split the input string into a list of strings, then convert to floats
arr = [float(x) for x in input_str.split()]

# Remove duplicates by converting to set and back to list
unique_arr = list(set(arr))

# Output the array with duplicates removed
print("Array with duplicates removed:", unique_arr)