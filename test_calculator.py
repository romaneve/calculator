"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 10 == calculator.divide(100, 10)

    def test_average(self):
        assert 200 == calculator.average((210, 190, 200))

    def test_handicap(self):
        assert 9.0 == calculator.handicap(220, .90, calculator.average((200,220,210)))
