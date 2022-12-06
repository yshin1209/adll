from neo4j import GraphDatabase as graphdb
from adll import graph

URI = "neo4j+s://34b10577.databases.neo4j.io"
USER = "neo4j"
PASSWORD = "A6uVT1wvZfAFLE_O9ilqxiHuDV30in887nHF-ByS_W0"

g = graph.Graph(graphdb, URI, USER, PASSWORD)

'''
g.add_node('DATA', 'name', 'x1')
g.set_node_prop('name', 'x1', 'value', 13)
g.add_node('Param', 'name', 'w1')
g.set_node_prop('name', 'w1', 'value', 2)
g.add_node('DATA', 'name', 'y1')
g.set_node_prop('name', 'y1', 'value', 0)
g.add_node('Math', 'mul_id', '1')
g.set_node_prop('mul_id', '1', 'name', 'mul')
g.add_node('Param', 'name', 'w2')
g.set_node_prop('name', 'w2', 'value', 3)
g.add_node('DATA', 'name', 'y2')
g.set_node_prop('name', 'y2', 'value', 0)
g.add_node('Math', 'mul_id', '2')
g.set_node_prop('mul_id', '2', 'name', 'mul')
g.add_edge('DATA2MATH', 'name', 'x1', 'mul_id', '1')
g.add_edge('PARAM2MATH', 'name', 'w1', 'mul_id', '1')
g.add_edge('MATH2DATA', 'mul_id', '1', 'name', 'y1')
g.add_edge('DATA2MATH', 'name', 'y1', 'mul_id', '2')
g.add_edge('PARAM2MATH', 'name', 'w2', 'mul_id', '2')
g.add_edge('MATH2DATA', 'mul_id', '2', 'name', 'y2')
print (g.get_node_prop('name', 'w1', 'value'))
'''
g.set_node_prop('name', 'x1', 'value', 6)
print (g.math_op('name', 'x1'))
print (g.get_node_prop('name', 'y1', 'value'))