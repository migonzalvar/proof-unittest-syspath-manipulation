import sys
import unittest

sys.path.append('/tmp')

class TestCase1(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1)
        self.assertTrue('/tmp' in sys.path)

