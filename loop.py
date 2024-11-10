# Prompt the user to enter an integer
num = int(input("Enter an integer: "))

# Initialize empty strings to store binary, octal, and hexadecimal representations
binary = ""
octal = ""
hexadecimal = ""

# Generate binary equivalent using a for loop and bitwise operators
for i in range(num.bit_length() - 1, -1, -1):
    binary += "1" if (num & (1 << i)) else "0"

# Generate octal equivalent using bitwise operators and a for loop
temp_num = num
while temp_num > 0:
    octal = str(temp_num & 7) + octal  # Use bitwise AND with 7 (0b111) to get last three bits
    temp_num >>= 3  # Shift right by 3 bits (equivalent to division by 8)

# Generate hexadecimal equivalent using bitwise operators and a for loop
temp_num = num
hex_chars = "0123456789ABCDEF"
while temp_num > 0:
    hexadecimal = hex_chars[temp_num & 15] + hexadecimal  # Use bitwise AND with 15 (0b1111) to get last four bits
    temp_num >>= 4  # Shift right by 4 bits (equivalent to division by 16)

# Display the results
print("Binary:", binary if binary else "0")
print("Octal:", octal if octal else "0")
print("Hexadecimal:", hexadecimal if hexadecimal else "0")
