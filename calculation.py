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

    def __str__(self):
        return f"{self.a} {self.operation} {self.b} = {self.result}"

    def get_result(self) -> float:
        """Returns the result of the calculation."""
        return self.result
