while True:
    # Prompt the user to enter a number or type 'exit' to quit
    user_input = input("Enter a number (or type 'exit' to quit): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break  # Exit the loop

    try:
        # Convert the input to a float
        number = float(user_input)

        # Determine if the number is positive, negative, or zero
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'exit' to quit.")
