from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "neo4j"
password = "neo4j1234!"
database_name = "neo4j"

driver = GraphDatabase.driver(uri, database=database_name, auth=(username, password))


def get_connected_nodes_any_label(tx, entity_text):
    query = """
    MATCH (e {text: $entity_text})-[r]-(other)
    RETURN e, type(r) AS relation, other
    """
    results = tx.run(query, entity_text=entity_text)
    connected_data = []
    for record in results:
        connected_data.append({
            "source_node": record["e"]._properties,
            "relation": record["relation"],
            "target_node": record["other"]._properties
        })
    return connected_data


def get_paths_any_label(tx, entity_text, max_depth=3):
    query = f"""
    MATCH p=(start {{text: $entity_text}})-[*1..{max_depth}]-(end)
    RETURN p
    """
    results = tx.run(query, entity_text=entity_text)
    paths = []
    for record in results:
        path_data = []
        for segment in record["p"].relationships:
            path_data.append({
                "start_node": segment.start_node._properties,
                "relation": segment._properties,
                "end_node": segment.end_node._properties
            })
        paths.append(path_data)
    return paths


def get_neighbors_any_label(entity_text):
    connected_data = []
    with driver.session() as session:
        connected_data = session.execute_read(get_connected_nodes_any_label, entity_text=entity_text)
    driver.close()
    return connected_data


def get_paths_from_entity_any_label(entity_text, max_depth=3):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    paths = []
    with driver.session() as session:
        paths = session.execute_read(get_paths_any_label, entity_text=entity_text, max_depth=max_depth)
    driver.close()
    return paths
