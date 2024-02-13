"""Importing unittest as its a built in unit tester for python making python a great choice for many complex functions"""
import unittest

"""Created a definition to store the number values in paramaters num1 & num2"""
def add_numbers(number1, number2):
    
    """Created a function that takes in the two paramaters and then adds the two together"""
    return number1 + number2

"""Main definiton holding the calulation part of things"""
def main():
    """Main function that calculates"""
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = add_numbers(number1, number2)
    print(f"The result of adding {number1} and {number2} is: {result}")

"Using a class to wrap Unittest.TestCase around the test function."
class TestAddNumbers(unittest.TestCase):
    """Created a definition for where the unit test takes place"""
    def test_add_numbers(self):
        """Pre built test model to test weather the function beind called when calculating the total sum is correctly executed"""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-5, -3), -8)

if __name__ == '__main__':
    main()
    unittest.main()
