import sys
import unittest


class TestCase2(unittest.TestCase):
    def test_two(self):
        self.assertEqual(2, 2)
        self.assertFalse('/tmp' in sys.path)

