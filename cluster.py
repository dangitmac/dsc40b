def cluster(graph, weights, level):
    visited_nodes = set()
    all_clusters = []

    for start_node in graph.nodes:
        if start_node not in visited_nodes:
            current_cluster = set()
            nodes_to_visit = [start_node]

            visited_nodes.add(start_node)

            while nodes_to_visit:
                current_node = nodes_to_visit.pop()
                current_cluster.add(current_node)

                for neighbor_node in graph.neighbors(current_node):
                    edge_weight = weights(current_node, neighbor_node)

                    if edge_weight >= level and neighbor_node not in visited_nodes:
                        visited_nodes.add(neighbor_node)
                        nodes_to_visit.append(neighbor_node)

            all_clusters.append(frozenset(current_cluster))

    return frozenset(all_clusters)
