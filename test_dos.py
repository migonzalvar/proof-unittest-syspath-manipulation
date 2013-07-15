import os.path
import sys
import unittest

ext_path = os.path.join(os.path.dirname(__file__), 'hidden')

class TestCase2(unittest.TestCase):
    def test_two(self):
        self.assertFalse(ext_path in sys.path)
        with self.assertRaises(ImportError):
            import module.spam
        self.assertEqual(2, 2)
