import unittest

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(cps3271(4), 16)


if __name__ == '__main__':
    unittest.main()
