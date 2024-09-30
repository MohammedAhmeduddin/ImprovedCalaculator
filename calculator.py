from calculation import Calculation
from history import History


class Calculator:
    """
    A class for performing basic arithmetic calculations.

    This class provides static methods for performing addition, subtraction,
    multiplication, and division. It also has a class method for adding
    calculations to the history.
    """

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the quotient of two numbers. 
        Raises ZeroDivisionError if the second number is zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

    @classmethod
    def add_calculation_to_history(cls, operation: str, a: float, b: float) -> Calculation:
        """
        Performs the given operation (add, subtract, multiply, divide), stores the result
        in the calculation history, and returns the calculation instance.
        """
        # Use a dictionary to map operations to functions
        operations = {
            'add': cls.add,
            'subtract': cls.subtract,
            'multiply': cls.multiply,
            'divide': cls.divide
        }

        # Error handling for invalid operations
        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")

        # Perform the operation and create a Calculation instance
        result = operations[operation](a, b)
        calc = Calculation(operation, a, b, result)
        History.add_to_history(calc)
        return calc

    