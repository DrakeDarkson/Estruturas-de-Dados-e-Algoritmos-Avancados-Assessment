import heapq

def dijkstra(graph, start, end):
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node == end:
            break
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    path, node = [], end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path.reverse()
    
    return path, distances[end]

graph = {
    'CD': [('A', 4), ('B', 2)],
    'A': [('C', 5), ('D', 10)],
    'B': [('A', 3), ('D', 8)],
    'C': [('D', 2), ('E', 4)],
    'D': [('E', 6), ('F', 5)],
    'E': [('F', 3)],
    'F': []
}

path, cost = dijkstra(graph, 'CD', 'F')
print("Rota ótima:", " -> ".join(path))
print("Distância mínima:", cost, "km")
