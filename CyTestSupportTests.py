import unittest
import CyTestSupport


class CyTestSupportTests(unittest.TestCase):

    def test_is_yes(self):
        self.assertTrue(CyTestSupport.TestUtils.is_yes('y'))
        self.assertTrue(CyTestSupport.TestUtils.is_yes('Y'))
        self.assertTrue(CyTestSupport.TestUtils.is_yes('yes'))
        self.assertTrue(CyTestSupport.TestUtils.is_yes('YES'))
        self.assertTrue(CyTestSupport.TestUtils.is_yes('yEs'))


if __name__ == '__main__':
    unittest.main()
