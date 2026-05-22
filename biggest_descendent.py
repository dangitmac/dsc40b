def biggest_descendent(graph, root, value):
    answer = {}

    def dfs(current_node):
        biggest_value = value[current_node]

        for child in graph.neighbors(current_node):
            child_biggest = dfs(child)
            biggest_value = max(biggest_value, child_biggest)

        answer[current_node] = biggest_value
        return biggest_value

    dfs(root)
    return answer
