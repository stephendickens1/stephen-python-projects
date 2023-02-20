# For: test_fizzbuzz.py
import unittest  # This is the default Python testing library, unittest

from fizzbuzz import fizzbuzz
# We import our generate function (def) from the fizzbuzz module (file)

class TestFizzbuzz(unittest.TestCase): 
    def test_fizz(self): 
        self.assertEqual(fizzbuzz(1), 1)


if __name__ == '__main__':
    unittest.main()