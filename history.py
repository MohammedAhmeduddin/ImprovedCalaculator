class History:
    history = []

    @classmethod
    def add_to_history(cls, calculation):
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls):
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()
        

