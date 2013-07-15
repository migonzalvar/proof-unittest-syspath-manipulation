import os.path
import sys
import unittest

ext_path = os.path.join(os.path.dirname(__file__), 'hidden')


def setUpModule():
    sys.path.append(ext_path)


def tearDownModule():
    sys.path.remove(ext_path)
    del sys.modules['module']
    del sys.modules['module.spam']


class TestCase1(unittest.TestCase):
    def test_one(self):
        import module.spam
        self.assertEqual(1, 1)
        self.assertTrue(ext_path in sys.path)
        result = module.spam.foo()
        self.assertEqual(result, 'bar')
        del module.spam

