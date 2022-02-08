import unittest
import hashlib
from app.functions import hashlines, getvactext


class TestHashLines(unittest.TestCase):
    def testhashingeq(self):
        self.assertEqual(hashlines('abc'), hashlib.sha256(str.encode('abc', 'UTF-8')).digest())

    def testhashingneq(self):
        assert_str = b'123'
        self.assertNotEqual(hashlines('abc'), assert_str)


class TestVacString(unittest.TestCase):
    def testvacstring(self):
        assert_str = 'Стажёр-программист Python / Python Developer Trainee вилка 29000 67000'
        self.assertEqual(getvactext(), assert_str)