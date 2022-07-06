import unittest
from main import add_fun


class TestFileName(unittest.TestCase):
    def test_add_fun(self):
        self.assertEqual(add_fun(1,5), 6)

if __name__ == '__main__':
    unittest.main()