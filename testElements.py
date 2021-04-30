import unittest
import elements

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(elements.calcElements([3,4,5]), 4)
    def test2(self):
        self.assertEqual(elements.calcElements([7,13,4]), 8)
    def test3_fail(self):
        self.assertEqual(elements.calcElements([1,8,6]), 4)

if __name__ == "__main__":
    unittest.main()