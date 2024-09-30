import argparse
from calculator import Calculator

def is_float(value):
    """Custom function to check if input is a valid float."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid number input: '{value}' is not a valid number.")

def main():
    # Set up argument parsing, treating inputs as strings initially
    parser = argparse.ArgumentParser(description="Simple Calculator Program")
    parser.add_argument("a", type=str, help="First number")
    parser.add_argument("b", type=str, help="Second number")
    parser.add_argument("operation", type=str, help="Operation (add, subtract, multiply, divide)")

    args = parser.parse_args()

    try:
        # Manually convert a and b to float using the custom validation function
        a = is_float(args.a)
        b = is_float(args.b)

        # Define a dictionary to map operations to functions
        operations = {
            'add': Calculator.add,
            'subtract': Calculator.subtract,
            'multiply': Calculator.multiply,
            'divide': Calculator.divide
        }

        operation_func = operations.get(args.operation)

        if not operation_func:
            raise ValueError(f"Unknown operation: {args.operation}")

        result = operation_func(a, b)
        print(f"The result of {a} {args.operation} {b} is {result}")

    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


