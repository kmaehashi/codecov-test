import unittest
import sys

from mylib.app import App

class TestApp(unittest.TestCase):
    def test_add(self):
        if sys.version_info[0] == 3:
            self.assertEqual(3, App().add(1, 2))

    def test_sub(self):
        if sys.version_info[0] == 2:
            self.assertEqual(-1, App().sub(1, 2))

    def test_mul(self):
        self.assertEqual(2, App().mul(1, 2))
