import unittest


class TestCore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # procedures before tests are started. This code block is executed only once
        pass

    @classmethod
    def tearDownClass(cls):
        # procedures after tests are finished. This code block is executed only once
        pass

    def setUp(self):
        # procedures before every tests are started. This code block is executed every time
        pass

    def tearDown(self):
        # procedures after every tests are finished. This code block is executed every time
        pass

    def test_core(self):
        # one test case. here.
        # You must “test_” prefix always. Unless, unittest ignores
        pass

if __name__ == '__main__':
    unittest.main()
