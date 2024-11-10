# Get an input number from the user
user_input = input("Enter a number: ")

# Convert the input to different numeric data types
# Using int() to convert to an integer
int_value = int(float(user_input))  # Convert to float first to handle decimal input, then to integer

# Using float() to convert to a floating-point number
float_value = float(user_input)

# Using complex() to convert to a complex number
complex_value = complex(user_input)

# Display the converted values
print("Integer value:", int_value)
print("Float value:", float_value)
print("Complex value:", complex_value)
