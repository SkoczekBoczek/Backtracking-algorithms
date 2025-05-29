import math

def exportToTikz(graph, filename="graph.tex"):
    header = [
        "\\begin{tikzpicture}[",
        "    >={Stealth[black]},",
        "    node distance=2cm,",
        "    every node/.style={fill=red!50,circle,draw=black,minimum size=8mm},",
        "    every edge/.style={draw=black,thick},",
        "    scale=0.8, transform shape",
        "]"
    ]
    
    footer = [
        "\\end{tikzpicture}"
    ]

    try:
        with open(filename, "w") as file:
            file.write("\n".join(header) + "\n\n")
            
            nodes = sorted(graph.keys())
            numNodes = len(nodes)

            if numNodes == 0:
                raise ValueError("Graph is empty")
                
            radius = max(4, math.sqrt(numNodes) * 1.5)
            center = (radius, radius)
            angleStep = 360 / numNodes
            
            positions = {}
            for i, node in enumerate(nodes):
                angle = math.radians(i * angleStep)
                x = center[0] + radius * math.cos(angle)
                y = center[1] + radius * math.sin(angle)
                positions[node] = (x, y)
                file.write(f"    \\node ({node}) at ({x:.2f},{y:.2f}) {{{node}}};\n")
            
            file.write("\n")
            
            written_edges = set()
            for node in nodes:
                for neighbor in graph[node]:
                    edge = tuple(sorted((node, neighbor)))
                    if edge not in written_edges:
                        file.write(f"    \\path [-] ({node}) edge ({neighbor});\n")
                        written_edges.add(edge)

            file.write("\n" + "\n".join(footer) + "\n")
            
        print(f"Successfully exported to {filename}")
        return True
        
    except Exception as e:
        print(f"Export error: {str(e)}")
        return False