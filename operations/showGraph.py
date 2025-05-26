def printGraph(graph):
    print("Graph representation:")
    for node in sorted(graph.keys()):
        neighbors = ", ".join(str(neighbor) for neighbor in graph[node])
        print(f"{node}: {neighbors}")
    
