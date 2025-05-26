import sys
from graphCreation import createGraph
from operations.showGraph import printGraph
from operations.TickzpictureExport import exportToTikz
from operations.findEuler import findEulerCycle


def printMenu():
    print("========================================")
    print("{}        {}".format("Help", "Shows this menu"))
    print("{}        {}".format("Exit", "Exits the program (or ctrl+D)"))
    print("{}       {}".format("Print", "Prints the graph"))
    print("========================================")

def interactiveMode(graph):
    print("\nInteractive mode (type 'help' for commands.)")
    while True:
        try:
            command = input("action> ").strip().lower()
            if not command:
                continue
            if command == "help":
                printMenu()
            elif command == "exit":
                print("\nExiting...")
                sys.exit(0)
            elif command == "print":
                printGraph(graph)
            elif command == "euler":
                cycle = findEulerCycle(graph)
                if cycle:
                    print("Euler cycle:", cycle)
                else:
                    print("No Euler cycle exists in this graph.")
            elif command == "export":
                filename = input("filename> ")
                exportToTikz(graph, filename)
            else:
                print(f"Unknown command '{command}'")
        except EOFError:
            print("\nExiting...")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    graph = createGraph()
    interactiveMode(graph)