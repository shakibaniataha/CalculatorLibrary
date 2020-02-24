"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(1, 3)

    def test_subtraction(self):
        assert 5 == calculator.subtract(12, 7)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
