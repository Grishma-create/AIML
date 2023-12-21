def a_star(start, goal, graph, heuristic):
    open_set, closed_set = {start}, set()
    g, parents = {start: 0}, {start: None}

    while open_set:
        current = min(open_set, key=lambda x: g[x] + heuristic[x])

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            path.reverse()
            print(f"Path found: {path}")
            return path

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor not in open_set and neighbor not in closed_set:
                open_set.add(neighbor)
                parents[neighbor], g[neighbor] = current, g[current] + weight
            elif (new_cost := g[current] + weight) < g[neighbor]:
                parents[neighbor], g[neighbor] = current, new_cost
                closed_set.discard(neighbor)
                open_set.add(neighbor)

    print("Path doesn't Exist")
    return None

graph_nodes = {'A': [('B', 6), ('F', 3)], 'B': [('C', 3), ('D', 2)], 'C': [('D', 1), ('E', 5)],
               'D': [('C', 1), ('E', 8)], 'E': [('I', 5), ('J', 5)], 'F': [('G', 1), ('H', 7)],
               'G': [('I', 3)], 'H': [('I', 2)], 'I': [('E', 5), ('J', 3)]}

heuristic_dist = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0}

a_star('A', 'J', graph_nodes, heuristic_dist)
