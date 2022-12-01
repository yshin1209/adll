import unittest
from adll import adll
from neo4j import GraphDatabase as graphdb

uri = "neo4j+s://34b10577.databases.neo4j.io"
user = "neo4j"
password = "A6uVT1wvZfAFLE_O9ilqxiHuDV30in887nHF-ByS_W0"
g = al.Graph(graphdb, uri, user, password)
class TestAl (unittest.TestCase):
    def test_add_node(self):
        self.assertEqual(g.get_node_prop('name', 'YongJUN', 'name'), 'YongJUN2') 