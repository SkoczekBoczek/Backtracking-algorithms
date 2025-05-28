def findHamiltonianCycle(graph):
    n = len(graph)
    nodes = list(graph.keys())

    def backtrack(path, visited):
        if len(path) == n:
            if path[0] in graph[path[-1]]:
                return path + [path[0]]
            else:
                return None
        current = path[-1]
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = backtrack(path + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    for start in nodes:
        cycle = backtrack([start], {start})
        if cycle:
            return cycle
    return None