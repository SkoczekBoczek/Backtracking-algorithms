import time
import csv
import os
import matplotlib.pyplot as plt
from graphCreation import createHamiltonianGraph, createNonHamiltonianGraph
from operations.findEuler import findEulerCycle
from operations.findHamilton import findHamiltonianCycle

directoryTimeName = "TimeResults"
if not os.path.exists(directoryTimeName):
    os.makedirs(directoryTimeName)

directoryPlotName = "PlotsResults"
if not os.path.exists(directoryPlotName):
    os.makedirs(directoryPlotName)

def benchmarkHamiltonianGraphs(nValues, saturation, filename):
    eulerTimes = []
    hamiltonTimes = []

    with open(os.path.join(directoryTimeName, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["n", "EulerTime", "HamiltonTime"])

        for n in nValues:
            print(f"Generating Hamiltonian graph with n={n}")
            graph = createHamiltonianGraph(n, saturation)

            # Euler cycle time
            start = time.time()
            findEulerCycle(graph)
            eulerTime = time.time() - start
            eulerTimes.append(eulerTime)

            # Hamiltonian cycle time
            start = time.time()
            findHamiltonianCycle(graph)
            hamiltonTime = time.time() - start
            hamiltonTimes.append(hamiltonTime)

            writer.writerow([n, eulerTime, hamiltonTime])
            print(f"n={n}: Euler={eulerTime:.8f}s, Hamilton={hamiltonTime:.8f}s")

    return eulerTimes, hamiltonTimes

def benchmarkNonHamiltonianGraphs(nValues, filename):
    hamiltonTimes = []

    with open(os.path.join(directoryTimeName, filename), mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["n", "HamiltonTime"])

        for n in nValues:
            print(f"Generating non-Hamiltonian graph with n={n}")
            graph = createNonHamiltonianGraph(n)

            start = time.time()
            result = findHamiltonianCycle(graph)
            hamiltonTime = time.time() - start
            hamiltonTimes.append(hamiltonTime)

            writer.writerow([n, hamiltonTime])
            print(f"n={n}: Hamilton={hamiltonTime:.8f}s")

    return hamiltonTimes

def plotResults(nValues, yValues, title, ylabel, filename=None):
    plt.figure(figsize=(10, 6))
    plt.plot(nValues, yValues, marker='o')
    plt.title(title)
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    if filename:
        plt.savefig(os.path.join(directoryPlotName, filename))
    # plt.show()

if __name__ == "__main__":
    nValsHam = list(range(10, 101, 10))
    print("Benchmarking Hamiltonian graphs")
    eulerT, hamiltonT = benchmarkHamiltonianGraphs(
        nValsHam, 
        saturation=30, 
        filename="resultHamiltonian.csv"
    )
    
    plotResults(nValsHam, eulerT, 
                'Czas znajdowania cyklu Eulera', 
                'Czas [s]', 'eulerHamiltonian.pdf')
    
    plotResults(nValsHam, hamiltonT, 
                'Czas znajdowania cyklu Hamiltona', 
                'Czas [s]', 'hamiltonHamiltonian.pdf')

    nValsNonHam = [10, 11, 12, 13, 14, 15, 16]
    print("\nBenchmarking non-Hamiltonian graphs")
    nonHamiltonT = benchmarkNonHamiltonianGraphs(
        nValsNonHam, 
        filename="resultNonHamiltonian.csv"
    )
    
    plotResults(nValsNonHam, nonHamiltonT, 
                'Czas znajdowania cyklu Hamliltona w grafie nie-hamiltonowskim', 
                'Czas [s]', 'hamiltonNonHamiltonian.pdf')