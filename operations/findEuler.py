# Algorytm Hierholzera
def findEulerCycle(graph):
    for node in graph:
        if len(graph[node]) % 2 != 0:
            print(f"Vertex {node} has an odd degree. Euler cycle does not exist.")
            return None

    localGraph = {u: list(vs) for u, vs in graph.items()}
    print(localGraph)
    stack = []
    circuit = []
    current = next((node for node in localGraph if localGraph[node]), None)

    if current is None:
        print("No edges in the graph.")
        return None

    stack.append(current)

    print(localGraph[current])
    while stack:
        if localGraph[current]:
            stack.append(current)
            neighbor = localGraph[current].pop()
            localGraph[neighbor].remove(current)
            current = neighbor
        else:
            circuit.append(current)
            current = stack.pop()

    return circuit[::-1]