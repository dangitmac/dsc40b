def slc(graph, d, k):

    all_nodes = list(graph.nodes)
    all_edges = list(graph.edges)

    parent = {}
    cluster_size = {}

    for node in all_nodes:
        parent[node] = node
        cluster_size[node] = 1

    def find_leader(node):

        while parent[node] != node:
            node = parent[node]
        return node

    def merge_clusters(node_one, node_two):

        leader_one = find_leader(node_one)
        leader_two = find_leader(node_two)

        if leader_one == leader_two:
            return False

        if cluster_size[leader_one] < cluster_size[leader_two]:
            parent[leader_one] = leader_two
            cluster_size[leader_two] += cluster_size[leader_one]
        else:
            parent[leader_two] = leader_one
            cluster_size[leader_one] += cluster_size[leader_two]

        return True

    edges_by_distance = sorted(all_edges, key=d)

    number_of_clusters = len(all_nodes)

    for edge in edges_by_distance:
        if number_of_clusters == k:
            break

        node_one, node_two = tuple(edge)

        merged = merge_clusters(node_one, node_two)

        if merged:
            number_of_clusters -= 1

    clusters_by_leader = {}

    for node in all_nodes:
        leader = find_leader(node)

        if leader not in clusters_by_leader:
            clusters_by_leader[leader] = set()

        clusters_by_leader[leader].add(node)

    final_clusters = set()

    for cluster in clusters_by_leader.values():
        final_clusters.add(frozenset(cluster))

    return frozenset(final_clusters)
