import time
import random

def movimentos_validos(x, y, tamanho, tabuleiro):
    movimentos = [
        (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)
    ]
    return [(nx, ny) for nx, ny in movimentos if 0 <= nx < tamanho and 0 <= ny < tamanho and tabuleiro[nx][ny] == -1]

def tour_forca_bruta(x, y, mov, tabuleiro, tamanho):
    if mov == tamanho * tamanho:
        return True
    for nx, ny in movimentos_validos(x, y, tamanho, tabuleiro):
        tabuleiro[nx][ny] = mov
        if tour_forca_bruta(nx, ny, mov + 1, tabuleiro, tamanho):
            return True
        tabuleiro[nx][ny] = -1
    return False

def heuristica_menor_grau(x, y, tamanho, tabuleiro):
    for mov in range(1, tamanho * tamanho):
        movimentos = movimentos_validos(x, y, tamanho, tabuleiro)
        if not movimentos:
            return False
        nx, ny = min(movimentos, key=lambda pos: len(movimentos_validos(pos[0], pos[1], tamanho, tabuleiro)))
        tabuleiro[nx][ny] = mov
        x, y = nx, ny
    return True

def resolver_problema(tamanho):
    tabuleiro = [[-1] * tamanho for _ in range(tamanho)]
    x, y = random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)
    tabuleiro[x][y] = 0
    
    start_time = time.perf_counter()
    forca_bruta = tour_forca_bruta(x, y, 1, tabuleiro, tamanho)
    end_time = time.perf_counter()
    tempo_forca_bruta = end_time - start_time
    
    tabuleiro = [[-1] * tamanho for _ in range(tamanho)]
    tabuleiro[x][y] = 0
    start_time = time.perf_counter()
    heuristica = heuristica_menor_grau(x, y, tamanho, tabuleiro)
    end_time = time.perf_counter()
    tempo_heuristica = end_time - start_time
    
    print(f"\nTabuleiro {tamanho}x{tamanho}:")
    print(f"Força bruta: {'Sucesso' if forca_bruta else 'Falha'} | Tempo: {tempo_forca_bruta:.6f} s")
    print(f"Heurística do menor grau: {'Sucesso' if heuristica else 'Falha'} | Tempo: {tempo_heuristica:.6f} s")

for tamanho in [5, 8, 10]:
    resolver_problema(tamanho)
