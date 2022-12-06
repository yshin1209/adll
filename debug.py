from neo4j import GraphDatabase as graphdb
from adll import graph

URI = "neo4j+s://34b10577.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "A6uVT1wvZfAFLE_O9ilqxiHuDV30in887nHF-ByS_W0"

g = graph.Graph(graphdb, URI, USER, PASSWORD)
g.add_node('Node', 'id', '1')
g.add_node('Node', 'id', '2')
result = g.add_edge('Edge', 'id', '1', 'id', '2')
print (result)