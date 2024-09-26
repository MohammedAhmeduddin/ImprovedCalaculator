class History:
    """
    Manages the history of calculations.

    Methods:
        add_to_history(calculation): Adds a calculation to the history.
        get_last_calculation(): Returns the last calculation from the history.
        get_history(): Returns the entire history.
        clear_history(): Clears the history.
    """
    history = []

    @classmethod
    def add_to_history(cls, calculation):
        """Adds a calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        """Returns the last calculation from the history."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls):
        """Returns the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears the history of all calculations."""
        cls.history.clear()
        