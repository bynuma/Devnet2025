import unittest
from mathy import add_numbers

class TestAddNumbers(unittest.TestCase):                                                # The class name should be descriptive of what is being tested and should inherit from unittest.TestCase.
    
    def test_add_positive_numbers(self):                                                # The method name should start with 'test_' to indicate that it is a test case.
        self.assertEqual(add_numbers(3, 4), 7, "Should be 7 when adding 3 and 4")       # The assertEqual method checks if the result of add_numbers(3, 4) is equal to 7. If not, it will raise an AssertionError with the provided message.

if __name__ == "__main__":
    unittest.main()                                                                     # The unittest.main() function is called to run the tests when the script is executed directly.