from collections import deque

def assign_good_and_evil(graph):
    node_labels = {}

    for start_node in graph.nodes:
        if start_node in node_labels:
            continue

        node_labels[start_node] = 'good'
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            current_label = node_labels[current_node]

            if current_label == 'good':
                opposite_label = 'evil'
            else:
                opposite_label = 'good'

            for neighbor in graph.neighbors(current_node):
                if neighbor not in node_labels:
                    node_labels[neighbor] = opposite_label
                    queue.append(neighbor)
                else:
                    if node_labels[neighbor] == current_label:
                        return None

    return node_labels
