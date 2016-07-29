import unittest
from calculator import *


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.calc = Calc()

    def test_calculate_adds_two_integers(self):
        self.assertEqual(self.calc.calculate('2', '+', '5'), 7)

    def test_calculate_subtracts_two_intergers(self):
        self.assertEqual(self.calc.calculate('9', '-', '3'), 6)

    def test_calculate_divides_two_integers(self):
        self.assertEqual(self.calc.calculate('12', '/', '3'), 4)

    def test_calculate_modulates_two_integers(self):
        self.assertEqual(self.calc.calculate('10', '%', '3'), 1)

    def test_calculate_multipies_two_integers(self):
        self.assertEqual(self.calc.calculate('7', '*', '8'), 56)

    def test_counter_counts(self):
        self.calc.counter = 3
        self.calc.count()
        self.assertEqual(self.calc.counter, 4)

    def test_last_answer_gives_the_previous_answer(self):
        self.calc.calculate('2', '+', '4')

        self.assertEqual(self.calc.last_answer, 6)

    def test_set_variable_creates_variable(self):
        self.calc.set_variable("x", "7")
        self.assertEqual(self.calc.variable_dict['x'], 7)

    def test_variables_passed_to_functions_correctly(self):
        self.assertEqual(self.calc.calculate("x", "+", "5"), 12)
        self.assertEqual(self.calc.calculate("10", "+", "x"), 17)

if __name__ == '__main__':
    unittest.main()
