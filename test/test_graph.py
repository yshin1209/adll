"""Module for testing graph.py"""

import unittest
from neo4j import GraphDatabase as graphdb
from adll import graph

URI = "neo4j+s://34b10577.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "A6uVT1wvZfAFLE_O9ilqxiHuDV30in887nHF-ByS_W0"
g = graph.Graph(graphdb, URI, USER, PASSWORD)
class TestGraph (unittest.TestCase):
    """Class for testing graph.py"""
    def test_add_node(self):
        """Function for testing add_node"""
        # To be implemented

    def test_set_node_prop(self):
        """Function for testing set_node_prop"""
        g.add_node ('Person', 'name', 'Juno')
        result = g.set_node_prop('name', 'Juno', 'age', 18)
        self.assertEqual(result['age'], 18)


    def test_get_node_prop(self):
        """Function for testing get_node_prop"""
        g.add_node ('Person', 'name', 'Thomas')
        self.assertEqual(g.get_node_prop('name', 'Thomas', 'name'), 'Thomas')

if __name__ == '__main__':
    unittest.main()
