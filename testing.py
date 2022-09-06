import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(8, 8)

    def test_decrement(self):
        self.assertEqual(10, 100)

if __name__ == '__main__':
    unittest.main()