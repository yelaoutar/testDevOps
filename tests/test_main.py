import unittest
from src.main import saluer

class TestSaluer(unittest.TestCase):
    def test_message(self):
        self.assertEqual(saluer("Python"), "Bonjour, Python !")
