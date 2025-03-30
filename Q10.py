import numpy as np
import time

def prim_mst(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    selected[0] = True
    mst_edges = []
    total_cost = 0
    
    for _ in range(num_vertices - 1):
        min_cost = float('inf')
        u, v = -1, -1
        
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j] > 0 and graph[i][j] < min_cost:
                        min_cost = graph[i][j]
                        u, v = i, j
        
        if u != -1 and v != -1:
            mst_edges.append((u, v, min_cost))
            total_cost += min_cost
            selected[v] = True
    
    return mst_edges, total_cost

graph_small = np.array([
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
])

np.random.seed(42)
graph_large = np.random.randint(1, 100, size=(100, 100))
np.fill_diagonal(graph_large, 0)

start_time = time.perf_counter()
mst_small, cost_small = prim_mst(graph_small)
end_time = time.perf_counter()
time_taken_small = end_time - start_time

start_time = time.perf_counter()
mst_large, cost_large = prim_mst(graph_large)
end_time = time.perf_counter()
time_taken_large = end_time - start_time

print("Grafo pequeno:")
print("Arestas da MST:", mst_small)
print("Custo total da MST:", cost_small)
print(f"Tempo de execução: {time_taken_small:.6f} segundos")

print("\nGrafo grande:")
print("Custo total da MST:", cost_large)
print(f"Tempo de execução: {time_taken_large:.6f} segundos")
