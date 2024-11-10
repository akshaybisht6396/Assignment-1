# Prompt the user to enter the first number
num1 = int(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = int(input("Enter the second number: "))

# Check if both numbers are even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")

# Check if both numbers are odd
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")

# Otherwise, one is even and the other is odd
else:
    print("One number is even and the other is odd.")
