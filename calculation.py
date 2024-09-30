"""
This module defines the Calculation class, which represents a single arithmetic operation.
"""

class Calculation:
    """
    Represents a single arithmetic calculation, storing the operation, operands, and result.
    """

    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

        # Validate that a, b, and result are numeric
        self._validate_inputs()

    def _validate_inputs(self):
        """Private method to validate that operands and result are valid floats."""
        if not all(isinstance(x, (int, float)) for x in [self.a, self.b, self.result]):
            raise ValueError("Operands and result must be numeric values (int or float).")

    def __str__(self):
        """Returns a human-readable string representation of the calculation."""
        return f"{self.a} {self.operation} {self.b} = {self.result}"

    def get_result(self) -> float:
        """Returns the result of the calculation."""
        return self.result

    def __eq__(self, other):
        """Defines equality comparison between two Calculation objects."""
        if isinstance(other, Calculation):
            return (self.operation == other.operation and
                    self.a == other.a and
                    self.b == other.b and
                    self.result == other.result)
        return False

