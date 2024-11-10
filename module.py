# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average of the three numbers
average = (num1 + num2 + num3) / 3

# Display the result using the % method for string formatting
print("The average of the three numbers is: %.2f" % average)
