import unittest
import CyTestSupport
import os.path

cyCaller = CyTestSupport.CyCaller()


class CytoscapeEndToEndTests(unittest.TestCase):

    def test_version(self):
        result = cyCaller.get("/v1/version")
        self.assertEqual(result['cytoscapeVersion'], '3.7.0-SNAPSHOT')

    def test_all_apps_started(self):
        result = cyCaller.get("/v1")
        self.assertTrue(result['allAppsStarted'])

    def test_galfiltered(self):
        path = os.path.join("resources", "galFiltered.cys")
        abspath = os.path.abspath(path)
        result = cyCaller.get("/v1/session?file=" + abspath)
        self.assertEqual(result['file'], abspath)


if __name__ == '__main__':
    unittest.main()
