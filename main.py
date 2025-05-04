class BasicCalculator:
    def __init__(self):
        self._result = 0  # Encapsulated result, can't be accessed directly outside the class

    # Basic Operations
    def add(self, a, b):
        self._result = a + b
        return self._result

    def subtract(self, a, b):
        self._result = a - b
        return self._result

    def multiply(self, a, b):
        self._result = a * b
        return self._result

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        self._result = a / b
        return self._result

    def display_result(self):
        return f"Result: {self._result}"


import math

class AdvancedCalculator(BasicCalculator):
    def square_root(self, a):
        if a < 0:
            return "Error! Cannot take square root of a negative number."
        self._result = math.sqrt(a)
        return self._result

    def power(self, a, b):
        self._result = a ** b
        return self._result

    def modulo(self, a, b):
        self._result = a % b
        return self._result

