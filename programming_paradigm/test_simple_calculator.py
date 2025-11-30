# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        # Initialize the calculator instance, making it available to all test methods
        self.calc = SimpleCalculator()

    # --- Test Cases for add() ---

    def test_addition(self):
        """Test addition with two positive integers."""
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_addition_negative_numbers(self):
        """Test addition with two negative integers."""
        self.assertEqual(self.calc.add(-10, -5), -15)

    def test_addition_mixed_numbers(self):
        """Test addition with a positive and a negative integer."""
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)
        
    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)

    # --- Test Cases for subtract() ---

    def test_subtraction(self):
        """Test subtraction resulting in a positive number."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
    def test_subtraction_negative_result(self):
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtraction_mixed_numbers(self):
        """Test subtraction involving negative numbers."""
        self.assertEqual(self.calc.subtract(-10, 5), -15) # -10 - 5 = -15
        self.assertEqual(self.calc.subtract(10, -5), 15)  # 10 - (-5) = 15
        
    # --- Test Cases for multiply() ---

    def test_multiplication(self):
        """Test multiplication of two positive integers."""
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiplication_negative(self):
        """Test multiplication resulting in a negative number."""
        self.assertEqual(self.calc.multiply(-5, 4), -20)

    def test_multiplication_double_negative(self):
        """Test multiplication of two negative integers."""
        self.assertEqual(self.calc.multiply(-5, -4), 20)

    def test_multiplication_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(100, 0), 0)

    # --- Test Cases for divide() ---

    def test_division(self):
        """Test standard division resulting in an integer."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_float_result(self):
        """Test division resulting in a float."""
        self.assertEqual(self.calc.divide(10, 4), 2.5)

    def test_division_negative_result(self):
        """Test division involving a negative number."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)

    def test_division_by_zero_edge_case(self):
        """Test the critical edge case: division by zero."""
        # The calculator function is designed to return None for this case
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_by_number(self):
        """Test dividing zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0)

# The following lines are not necessary for running with 'python -m unittest' 
# but are included if the script were run directly.
if __name__ == '__main__':
    unittest.main()