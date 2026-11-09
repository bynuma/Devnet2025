import unittest                                                     # The unittest module is imported to provide a framework for writing and running tests in Python.
from main import calculate_rectangle_area

class TestRectangleArea(unittest.TestCase):                         # The class name should be descriptive of what is being tested and should inherit from unittest.TestCase.
    def test_positive_numbers(self):                                # The method name should start with 'test_' to indicate that it is a test case.
        self.assertEqual(calculate_rectangle_area(5, 4), 20)        # The assertEqual method checks if the result of calculate_rectangle_area(5, 4) is equal to 20. If not, it will raise an AssertionError.
        self.assertEqual(calculate_rectangle_area(2.5, 3.5), 8.75)
        
    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(0, 5)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, 0)
            
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5, 4)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5, -4)

if __name__ == '__main__':
    unittest.main() 