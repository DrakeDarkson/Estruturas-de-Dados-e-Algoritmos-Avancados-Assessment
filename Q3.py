class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()
    
    def inserir(self, palavra):
        nodo = self.raiz
        for char in palavra:
            if char not in nodo.filhos:
                nodo.filhos[char] = TrieNode()
            nodo = nodo.filhos[char]
        nodo.fim_palavra = True
    
    def buscar_prefixo(self, prefixo):
        nodo = self.raiz
        for char in prefixo:
            if char not in nodo.filhos:
                return None
            nodo = nodo.filhos[char]
        return nodo
    
    def autocompletar(self, prefixo):
        def coletar_palavras(nodo, prefixo, sugestoes):
            if nodo.fim_palavra:
                sugestoes.append(prefixo)
            for char, prox_nodo in nodo.filhos.items():
                coletar_palavras(prox_nodo, prefixo + char, sugestoes)
        
        nodo = self.buscar_prefixo(prefixo)
        sugestoes = []
        if nodo:
            coletar_palavras(nodo, prefixo, sugestoes)
        return sugestoes
    
    def correcao_automatica(self, palavra, limite_distancia=1):
        def distancia_levenshtein(a, b):
            if not a: return len(b)
            if not b: return len(a)
            
            if a[0] == b[0]:
                return distancia_levenshtein(a[1:], b[1:])
            
            inserir = 1 + distancia_levenshtein(a, b[1:])
            remover = 1 + distancia_levenshtein(a[1:], b)
            substituir = 1 + distancia_levenshtein(a[1:], b[1:])
            
            return min(inserir, remover, substituir)
        
        sugestoes = []
        def percorrer_trie(nodo, palavra_atual):
            if nodo.fim_palavra and distancia_levenshtein(palavra, palavra_atual) <= limite_distancia:
                sugestoes.append(palavra_atual)
            for char, prox_nodo in nodo.filhos.items():
                percorrer_trie(prox_nodo, palavra_atual + char)
        
        percorrer_trie(self.raiz, "")
        return sugestoes

trie = Trie()

while True:
    comando = input("Digite um comando (inserir, autocompletar, corrigir, sair): ")
    if comando == "inserir":
        titulo = input("Digite o título do livro: ")
        trie.inserir(titulo)
    elif comando == "autocompletar":
        prefixo = input("Digite o prefixo: ")
        print(trie.autocompletar(prefixo))
    elif comando == "corrigir":
        palavra = input("Digite a palavra: ")
        print(trie.correcao_automatica(palavra))
    elif comando == "sair":
        break
