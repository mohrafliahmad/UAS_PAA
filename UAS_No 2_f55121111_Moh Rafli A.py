import time
import itertools
import networkx as nx

def tsp(graph):
    start_time = time.time()
    nodes = list(graph.nodes)
    num_nodes = len(nodes)
    shortest_path = None
    shortest_distance = float('inf')

    for perm in itertools.permutations(nodes):
        distance = 0
        for i in range(num_nodes - 1):
            distance += graph[perm[i]][perm[i+1]]['weight']
        distance += graph[perm[-1]][perm[0]]['weight']

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = perm

        print(f"Iterasi: {perm} dengan jarak {distance}")

    end_time = time.time()
    computation_time = end_time - start_time
    print(f"Waktu komputasi: {computation_time} detik")
    print(f"Hasil akhir (shortest path): {shortest_path} dengan jarak {shortest_distance}")

def dijkstra(graph, start_node):
    start_time = time.time()
    shortest_paths = {}
    shortest_distances = {}

    shortest_paths[start_node], shortest_distances[start_node] = nx.single_source_dijkstra(graph, start_node)

    end_time = time.time()
    computation_time = end_time - start_time
    print(f"Waktu komputasi: {computation_time} detik")
    print("Hasil akhir (shortest path):")
    for node in shortest_paths:
        print(f"Node {node}: {shortest_paths[node]} dengan jarak {shortest_distances[node]}")

def main():
    # Membangun graf
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('B', 'C', weight=8)
    graph.add_edge('C', 'A', weight=10)
    graph.add_edge('B', 'D', weight=12)
    graph.add_edge('D', 'C', weight=11)
    graph.add_edge('C', 'E', weight=3)
    graph.add_edge('E', 'D', weight=11)
    graph.add_edge('C', 'G', weight=9)
    graph.add_edge('G', 'E', weight=7)
    graph.add_edge('G', 'A', weight=12)
    graph.add_edge('E', 'F', weight=6)
    graph.add_edge('F', 'G', weight=9)
    graph.add_edge('D', 'F', weight=10)

    print("Pilihan algoritma:")
    print("1. TSP")
    print("2. Dijkstra")

    choice = input("Pilih algoritma (1/2): ")

    if choice == "1":
        tsp(graph)
    elif choice == "2":
        start_node = input("Masukkan node awal: ")
        dijkstra(graph, start_node)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
