import unittest
from main import recursive_fibonacci


class DataCleaningTest(unittest.TestCase):
    """
    Tests the flow of data cleaning
    """
    def test_fibonacci(self):
        """
        Test data cleaning object creation
        """
        self.assertAlmostEqual(recursive_fibonacci(0), 0)
        self.assertAlmostEqual(recursive_fibonacci(1), 0)
        self.assertAlmostEqual(recursive_fibonacci(2), 1)
        self.assertAlmostEqual(recursive_fibonacci(3), 1)
        self.assertAlmostEqual(recursive_fibonacci(4), 2)
        self.assertAlmostEqual(recursive_fibonacci(10), 34)
        self.assertAlmostEqual(recursive_fibonacci(30), 514229)


if __name__ == '__main__':
    unittest.main()
