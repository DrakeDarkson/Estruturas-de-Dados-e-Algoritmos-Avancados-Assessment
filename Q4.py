class GrafoMatriz:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[float('inf')] * len(vertices) for _ in range(len(vertices))]
        for i in range(len(vertices)):
            self.matriz[i][i] = 0
    
    def adicionar_aresta(self, origem, destino, peso):
        i, j = self.vertices.index(origem), self.vertices.index(destino)
        self.matriz[i][j] = peso
        self.matriz[j][i] = peso
    
    def mostrar_matriz(self):
        for linha in self.matriz:
            print(linha)

class GrafoLista:
    def __init__(self):
        self.lista = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.lista:
            self.lista[vertice] = []
    
    def adicionar_aresta(self, origem, destino, peso):
        self.lista[origem].append((destino, peso))
        self.lista[destino].append((origem, peso))
    
    def mostrar_lista(self):
        for vertice, conexoes in self.lista.items():
            print(vertice, "->", conexoes)

bairros = ['A', 'B', 'C', 'D', 'E', 'F']
arestas = [('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 3),
           ('D', 'F', 6), ('E', 'F', 1)]

print("Matriz de Adjacência:")
grafo_matriz = GrafoMatriz(bairros)
for origem, destino, peso in arestas:
    grafo_matriz.adicionar_aresta(origem, destino, peso)
grafo_matriz.mostrar_matriz()

print("\nLista de Adjacência:")
grafo_lista = GrafoLista()
for bairro in bairros:
    grafo_lista.adicionar_vertice(bairro)
for origem, destino, peso in arestas:
    grafo_lista.adicionar_aresta(origem, destino, peso)
grafo_lista.mostrar_lista()
