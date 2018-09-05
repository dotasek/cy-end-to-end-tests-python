import unittest
import CyTestSupport
import os.path

try:
    # pylint: disable
    input = raw_input
except NameError:
    pass

cyCaller = CyTestSupport.CyCaller()

class CytoscapeEndToEndTests(unittest.TestCase):

    def test_version(self):
        result = cyCaller.get("/v1/version")
        self.assertEqual(result['cytoscapeVersion'], '3.7.0-SNAPSHOT')

    def test_all_apps_started(self):
        result = cyCaller.get("/v1")
        self.assertTrue(result['allAppsStarted'])

    def test_galfiltered(self):
        cyCaller.load_file('galFiltered.cys')
        suid = cyCaller.get_network_suid()

        edges = cyCaller.get("/v1/networks/"+str(suid)+"/edges")
        self.assertEqual(len(edges), 362)
        nodes = cyCaller.get("/v1/networks/"+str(suid)+"/nodes")
        self.assertEqual(len(nodes), 331)
        user_input = input("Is there a network of 331 nodes and 362 edges visible in Cytoscape (y/n)?")
        self.assertTrue(CyTestSupport.TestUtils.is_yes(user_input))

    def test_diffusion(self):
        cyCaller.load_file('galFiltered.cys')
        suid = cyCaller.get_network_suid()
        rows = cyCaller.get("/v1/networks/" + str(suid) + "/tables/defaultnode/rows")
        node_suid = -1
        for row in rows:
            if row['COMMON'] == 'RAP1':
                node_suid = row['SUID']
                break
        selected_nodes = [node_suid]
        cyCaller.put("/v1/networks/"+str(suid) + "/nodes/selected", selected_nodes)
        cyCaller.post("/diffusion/v1/currentView/diffuse", None)
        user_input = input("Has Diffusion run and selected more nodes? (y/n)")
        self.assertTrue(CyTestSupport.TestUtils.is_yes(user_input))

    def test_layout(self):
        cyCaller.load_file('galFiltered.cys')
        suid = cyCaller.get_network_suid()
        cyCaller.get("/v1/apply/layouts/circular/" + str(suid))
        user_input = input("Has the network been laid out using the circular layout? (y/n)")
        self.assertTrue(CyTestSupport.TestUtils.is_yes(user_input))


if __name__ == '__main__':
    unittest.main()
