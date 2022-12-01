import unittest
from neo4j import GraphDatabase as graphdb
from adll import graph

URI = "neo4j+s://34b10577.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "A6uVT1wvZfAFLE_O9ilqxiHuDV30in887nHF-ByS_W0"
g = graph.Graph(graphdb, URI, USER, PASSWORD)
class TestGraph (unittest.TestCase):
    def test_add_node(self):
        self.assertEqual(g.get_node_prop('name', 'JungJai2', 'name'), 'JungJai2')

if __name__ == '__main__':
    unittest.main()