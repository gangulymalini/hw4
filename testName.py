import unittest
import name

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.generateName("beyonce", "knowles"), "beyonce knowles")
    def test2(self):
        self.assertEqual(name.generateName("malini", "ganguly"), "malini ganguly")
    def test3_fail(self):
        self.assertEqual(name.generateName("mariah", "carey"), "random")

if __name__ == "__main__":
    unittest.main()