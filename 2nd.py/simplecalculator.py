def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulo (%)")
        print("6. Exit")

        # Get user's choice
        choice = input("Enter the number corresponding to your operation (1-5): ")

        if choice == '6':  
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4','5']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                # Perform operation
                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result is: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
                elif choice =='5':
                    print(f"The result is: {num1 % num2}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
calculator()