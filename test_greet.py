import unittest
from greet import greet


class GreetTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
