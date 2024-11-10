# Get user's first and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Use the strip() method to remove any leading/trailing spaces from input
first_name = first_name.strip()
last_name = last_name.strip()

# Reverse the strings using slicing and capitalize() to format the names properly
reversed_first = first_name[::-1].capitalize()  # Reverses first name and capitalizes the first letter
reversed_last = last_name[::-1].capitalize()    # Reverses last name and capitalizes the first letter

# Print the reversed names with a space in between
print(reversed_last, reversed_first)
