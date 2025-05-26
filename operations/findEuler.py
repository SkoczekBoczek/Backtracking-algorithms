def findEulerCycle(graph):
    # Sprawdź warunek konieczny: wszystkie stopnie parzyste
    for node in graph:
        if len(graph[node]) % 2 != 0:
            return None  # Cykl Eulera nie istnieje

    # Skopiuj graf, aby nie modyfikować oryginału
    temp_graph = {u: list(vs) for u, vs in graph.items()}
    stack = []
    cycle = []

    # Znajdź pierwszy wierzchołek z krawędziami
    start = next((node for node in temp_graph if temp_graph[node]), None)
    if start is None:
        return None

    stack.append(start)
    while stack:
        v = stack[-1]
        if temp_graph[v]:
            u = temp_graph[v].pop()
            temp_graph[u].remove(v)
            stack.append(u)
        else:
            cycle.append(stack.pop())

    # Cykl Eulera powinien odwiedzić wszystkie krawędzie
    if any(temp_graph[node] for node in temp_graph):
        return None

    return cycle[::-1]  # Odwróć, by uzyskać poprawną kolejność