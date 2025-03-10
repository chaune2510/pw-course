import unittest

class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        print("I will run once before every test!")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every test!")

if __name__ == '__main__':
    unittest.main(verbosity=2)