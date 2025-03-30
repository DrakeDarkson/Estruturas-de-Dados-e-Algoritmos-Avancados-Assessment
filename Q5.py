from collections import deque

class MetroGraph:
    def __init__(self):
        self.graph = {}

    def add_connection(self, station1, station2):
        if station1 not in self.graph:
            self.graph[station1] = []
        if station2 not in self.graph:
            self.graph[station2] = []
        self.graph[station1].append(station2)
        self.graph[station2].append(station1)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
        return visited

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            station = queue.popleft()
            if station not in visited:
                visited.add(station)
                queue.extend(neighbor for neighbor in self.graph[station] if neighbor not in visited)
        return visited

metro = MetroGraph()
connections = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('D', 'E'), ('E', 'F')
]
for station1, station2 in connections:
    metro.add_connection(station1, station2)

dfs_result = metro.dfs('A')
bfs_result = metro.bfs('A')

print("DFS:", dfs_result)
print("BFS:", bfs_result)
