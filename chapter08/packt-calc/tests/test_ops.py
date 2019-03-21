import unittest

from packt_calc.calc import add, sub
from aiohttp.web import Request

class TestOps(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(3, 2))

    def test_sub(self):
        self.assertEqual(3, sub(8, 5))