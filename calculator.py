# calculator.py
# Mini project - Day 8 task
# Simple calculator that performs basic arithmetic operations

print("=== Simple Calculator ===")

# Get input from user
try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, /, %, **): ")
    num2 = float(input("Enter the second number: "))

    # Perform calculation based on operator
    result = None

    if operator == '+':
        result = num1 + num2
        operation = "addition"
    elif operator == '-':
        result = num1 - num2
        operation = "subtraction"
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = num1 / num2
            operation = "division"
    elif operator == '%':
        if num2 == 0:
            print("Error: Modulo by zero is not allowed!")
        else:
            result = num1 % num2
            operation = "modulo"
    elif operator == '**':
        result = num1 ** num2
        operation = "exponentiation"
    else:
        print(f"Error: '{operator}' is not a valid operator!")

    # Display result if calculation was successful
    if result is not None:
        print(f"\nResult of {operation}:")
        print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numbers!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\nThank you for using the calculator!")
