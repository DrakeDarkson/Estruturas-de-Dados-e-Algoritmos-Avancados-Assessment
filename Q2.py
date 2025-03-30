import heapq

class Pacote:
    def __init__(self, id_pacote, prioridade, tempo_transmissao):
        self.id_pacote = id_pacote
        self.prioridade = prioridade
        self.tempo_transmissao = tempo_transmissao
    
    def __lt__(self, outro):
        return self.prioridade < outro.prioridade

class Roteador:
    def __init__(self):
        self.fila_prioridade = []
        self.pacotes = {}
    
    def inserir_pacote(self, id_pacote, prioridade, tempo_transmissao):
        pacote = Pacote(id_pacote, prioridade, tempo_transmissao)
        heapq.heappush(self.fila_prioridade, pacote)
        self.pacotes[id_pacote] = pacote
    
    def remover_pacote(self):
        if self.fila_prioridade:
            pacote = heapq.heappop(self.fila_prioridade)
            del self.pacotes[pacote.id_pacote]
            return f"Transmitindo pacote {pacote.id_pacote} (Prioridade: {pacote.prioridade})"
        return "Nenhum pacote para transmitir"
    
    def atualizar_prioridade(self, id_pacote, nova_prioridade):
        if id_pacote in self.pacotes:
            self.pacotes[id_pacote].prioridade = nova_prioridade
            self.fila_prioridade = list(self.pacotes.values())
            heapq.heapify(self.fila_prioridade)

roteador = Roteador()
roteador.inserir_pacote(101, 3, 5)
roteador.inserir_pacote(102, 1, 2)
roteador.inserir_pacote(103, 2, 3)

print(roteador.remover_pacote())
roteador.atualizar_prioridade(103, 0)
print(roteador.remover_pacote())
