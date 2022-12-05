# Graph class
"""Module providing basic graph queries (Neo4j Cypher)"""

class Graph:
    """Class for providing basic graph queries (Neo4j Cypher)"""
    # Initialize graph database class
    def __init__(self, graphdb, uri, user, password):
        self.driver = graphdb.driver(uri, auth=(user, password))

    # Close session
    def close(self)-> None:
        """Function for session closing"""
        self.driver.close()

    # Add node
    @staticmethod
    def _add_node_tx(tx, node_label, key, value):
        query = "MERGE (n:" + node_label + "{ " + key + ": $value })" \
                " RETURN n"
        result = tx.run(query, value = value)
        return result.single()[0]

    def add_node(self, node_label, key, value):
        """Function for adding node"""

        # Check if the parameter types are correct
        if not isinstance (node_label, str):
            raise TypeError ("The first argument (node label) must be a string")
        if not isinstance (key, str):
            raise TypeError ("The second argument (key) must be a string")
        # neo4j property value types: https://neo4j.com/docs/cypher-manual/current/syntax/values/

        with self.driver.session() as session:
            result = session.execute_write(self._add_node_tx, node_label, key, value)
            return result

    # Delete node
    @staticmethod
    def _delete_node_tx(tx, node_label, key, value):
        query = "MERGE (n:" + node_label + "{ " + key + ": $value })" \
                " DELETE n"
        result = tx.run(query, value = value)
        return result.single()[0]

    def delete_node(self, node_label, key, value):
        """Function for adding node"""

        # Check if the parameter types are correct
        if not isinstance (node_label, str):
            raise TypeError ("The first argument (node label) must be a string")
        if not isinstance (key, str):
            raise TypeError ("The second argument (key) must be a string")
        # neo4j property value types: https://neo4j.com/docs/cypher-manual/current/syntax/values/

        with self.driver.session() as session:
            result = session.execute_write(self._delete_node_tx, node_label, key, value)
            return result

    # Set node property value
    @staticmethod
    def _set_node_prop_tx(tx, id_key, id_value, key, value):
        query = "MATCH (n) WHERE n." + id_key + " = $id_value" \
                " SET n." + key + " = $value" \
                " RETURN n"
        result = tx.run(query, id_value = id_value, value = value)
        return result.single()[0]

    def set_node_prop(self, id_key, id_value, key, value):
        """Function for setting node property value"""
        with self.driver.session() as session:
            result = session.execute_write(self._set_node_prop_tx, id_key, id_value, key, value)
            return result

    # Get node property value
    @staticmethod
    def _get_node_prop_tx(tx, id_key, id_value, key ):
        query = "MATCH (n) WHERE n." + id_key + " = $id_value" \
                " RETURN n." + key + " as value"
        result = tx.run(query, id_value = id_value)
        return result.single()[0]

    def get_node_prop(self, id_key, id_value, key):
        """Function for getting node property value"""
        with self.driver.session() as session:
            result = session.execute_write(self._get_node_prop_tx, id_key, id_value, key)
            return result
