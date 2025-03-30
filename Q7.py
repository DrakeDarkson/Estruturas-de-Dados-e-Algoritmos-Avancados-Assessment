import numpy as np

def floyd_warshall(bairros, conexoes):
    n = len(bairros)
    INF = float('inf')
    matriz_distancia = np.full((n, n), INF)
    np.fill_diagonal(matriz_distancia, 0)
    
    for (origem, destino), tempo in conexoes.items():
        i, j = bairros.index(origem), bairros.index(destino)
        matriz_distancia[i][j] = tempo
        matriz_distancia[j][i] = tempo
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz_distancia[i][j] = min(matriz_distancia[i][j], matriz_distancia[i][k] + matriz_distancia[k][j])
    
    return matriz_distancia

bairros = ['A', 'B', 'C', 'D', 'E', 'F']
conexoes = {
    ('A', 'B'): 5, ('A', 'C'): 10,
    ('B', 'C'): 3, ('B', 'D'): 8,
    ('C', 'D'): 2, ('C', 'E'): 7,
    ('D', 'E'): 4, ('D', 'F'): 6,
    ('E', 'F'): 5
}

resultado = floyd_warshall(bairros, conexoes)
print("Matriz de menores tempos entre os bairros:")
print(resultado)
