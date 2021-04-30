import unittest
import volume

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(volume.calcVolume(5), 125)
    def test2(self):
        self.assertEqual(volume.calcVolume(-1), -1)
    def test3(self):
        self.assertEqual(volume.calcVolume(20), 8000)

if __name__ == "__main__":
    unittest.main()