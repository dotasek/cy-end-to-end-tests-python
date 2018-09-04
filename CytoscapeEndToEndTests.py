import unittest
import CyTestSupport

cyCaller = CyTestSupport.CyCaller()


class CytoscapeEndToEndTests(unittest.TestCase):

    def test_upper(self):
        result = cyCaller.get("/v1/version")
        self.assertEqual(result['cytoscapeVersion'], '3.7.0-SNAPSHOT')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])


if __name__ == '__main__':
    unittest.main()
