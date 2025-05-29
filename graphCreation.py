import sys
import re
import random
from collections import defaultdict

def createNonHamiltonianGraph(vertices):
    nodes = list(range(1, vertices + 1))
    graph = defaultdict(list)

    isolated = nodes[-1] # Last node is isolated
    activeNodes = nodes[:-1] # Nodes without the last one

    totalPossibleEdges = len(activeNodes) * (len(activeNodes) - 1) // 2
    desiredEdges = int(0.5 * totalPossibleEdges)
    edges = set()

    while len(edges) < desiredEdges:
        u, v = random.sample(activeNodes, 2)
        edge = tuple(sorted((u, v)))
        if edge not in edges:
            edges.add(edge)
            graph[u].append(v)
            graph[v].append(u)
        
    graph[isolated] = []

    return dict(graph)


def createHamiltonianGraph(vertices, saturation):
    nodes = list(range(1, vertices + 1))
    random.shuffle(nodes)
    graph = defaultdict(list)
    edges = set()

    # Create a Hamiltonian cycle
    for i in range(len(nodes)):
        u = nodes[i]
        v = nodes[(i + 1) % len(nodes)]
        edge = tuple(sorted((u, v)))
        if edge not in edges:
            edges.add(edge)
            graph[u].append(v)
            graph[v].append(u)

    # Add random edges to achieve the desired saturation
    totalPossibleEdges = vertices * (vertices - 1) // 2
    desiredEdges = int((saturation / 100) * totalPossibleEdges)
    currentEdges = len(edges)

    while currentEdges < desiredEdges:
        u, v = random.sample(nodes, 2)
        edge = tuple(sorted((u, v)))
        if edge not in edges:
            edges.add(edge)
            graph[u].append(v)
            graph[v].append(u)
            currentEdges += 1

    # Ensure all nodes have even degree
    oddNodes = [node for node in nodes if len(graph[node]) % 2 != 0]
    while len(oddNodes) >= 2:
        u = oddNodes.pop()
        for i, v in enumerate(oddNodes):
            edge = tuple(sorted((u, v)))
            if edge not in edges:
                edges.add(edge)
                graph[u].append(v)
                graph[v].append(u)
                oddNodes.pop(i)
                break

    return dict(graph)

def createGraph():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--hamilton", "--non-hamilton"]:
        print("Usage: python3 main.py --hamilton")
        print("Or:    python3 main.py --non-hamilton")
        sys.exit(1)

    hamilton = sys.argv[1]
    print("Enter the number of vertices")
    while True:
        try:
            node = int(input("vertices> ").strip())
            if node < 10:
                print("Hamiltonian and non-Hamiltonian graphs require at least 10 vertices.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer for the number of vertices.")
            continue
        break

    if hamilton == "--hamilton":
        while True:
            try:
                saturation = int(input("saturation> ").strip())
                if saturation != 30 and saturation != 70:
                    print("Saturation must be either 30 or 70.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter integers for vertices and saturation.")
                continue
        print("Creating a Hamiltonian graph...")
        graph = createHamiltonianGraph(node, saturation)
        return graph
    
    elif hamilton == "--non-hamilton":
        print("Creating a non-Hamiltonian graph...")
        graph = createNonHamiltonianGraph(node)
        return graph
    return None