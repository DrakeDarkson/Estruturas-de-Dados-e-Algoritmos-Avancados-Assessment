import itertools
import random
import time
import numpy as np

def calcular_distancia(caminho, matriz_dist):
    return sum(matriz_dist[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1)) + matriz_dist[caminho[-1]][caminho[0]]

def tsp_forca_bruta(matriz_dist):
    n = len(matriz_dist)
    menor_custo = float('inf')
    melhor_rota = None
    for perm in itertools.permutations(range(n)):
        custo = calcular_distancia(perm, matriz_dist)
        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = perm
    return melhor_rota, menor_custo

def tsp_vizinho_mais_proximo(matriz_dist):
    n = len(matriz_dist)
    visitados = [False] * n
    caminho = [0]
    visitados[0] = True
    
    for _ in range(n - 1):
        ultimo = caminho[-1]
        proximo = min(((i, matriz_dist[ultimo][i]) for i in range(n) if not visitados[i]), key=lambda x: x[1])[0]
        caminho.append(proximo)
        visitados[proximo] = True
    return caminho, calcular_distancia(caminho, matriz_dist)

def criar_matriz_dist(n):
    matriz = [[random.randint(10, 100) if i != j else 0 for j in range(n)] for i in range(n)]
    return matriz

def avaliar_populacao(populacao, matriz_dist):
    return sorted([(ind, calcular_distancia(ind, matriz_dist)) for ind in populacao], key=lambda x: x[1])

def cruzamento(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 2)
    filho = pai1[:ponto_corte] + [x for x in pai2 if x not in pai1[:ponto_corte]]
    return filho

def mutacao(individuo):
    i, j = random.sample(range(len(individuo)), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]

def tsp_genetico(matriz_dist, tamanho_pop=100, geracoes=100):
    n = len(matriz_dist)
    populacao = [random.sample(range(n), n) for _ in range(tamanho_pop)]
    
    for _ in range(geracoes):
        populacao = avaliar_populacao(populacao, matriz_dist)
        nova_populacao = [ind for ind, _ in populacao[:10]]
        while len(nova_populacao) < tamanho_pop:
            p1, p2 = random.sample(populacao[:50], 2)
            filho = cruzamento(p1[0], p2[0])
            if random.random() < 0.1:
                mutacao(filho)
            nova_populacao.append(filho)
        populacao = nova_populacao
    
    melhor_rota, menor_custo = avaliar_populacao(populacao, matriz_dist)[0]
    return melhor_rota, menor_custo

for tamanho in [4, 6, 10]:
    matriz_dist = criar_matriz_dist(tamanho)
    
    start = time.time()
    rota_forca_bruta, custo_forca_bruta = tsp_forca_bruta(matriz_dist) if tamanho <= 6 else (None, None)
    tempo_forca_bruta = time.time() - start
    
    start = time.time()
    rota_vizinho, custo_vizinho = tsp_vizinho_mais_proximo(matriz_dist)
    tempo_vizinho = time.time() - start
    
    start = time.time()
    rota_genetico, custo_genetico = tsp_genetico(matriz_dist)
    tempo_genetico = time.time() - start
    
    print(f"\nTSP com {tamanho} cidades:")
    if rota_forca_bruta:
        print(f"Força Bruta: Custo = {custo_forca_bruta}, Tempo = {tempo_forca_bruta:.6f}s")
    print(f"Vizinho Mais Próximo: Custo = {custo_vizinho}, Tempo = {tempo_vizinho:.6f}s")
    print(f"Algoritmo Genético: Custo = {custo_genetico}, Tempo = {tempo_genetico:.6f}s")
