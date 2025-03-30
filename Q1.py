import heapq

class Processo:
    def __init__(self, pid, tempo_execucao, prioridade):
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade
    
    def __lt__(self, outro):
        return self.prioridade < outro.prioridade

class Escalonador:
    def __init__(self):
        self.fila_prioridade = []
        self.processos = {}
    
    def adicionar_processo(self, pid, tempo_execucao, prioridade):
        processo = Processo(pid, tempo_execucao, prioridade)
        heapq.heappush(self.fila_prioridade, processo)
        self.processos[pid] = processo
    
    def executar_proximo(self):
        if self.fila_prioridade:
            processo = heapq.heappop(self.fila_prioridade)
            del self.processos[processo.pid]
            return f"Executando processo {processo.pid} (Prioridade: {processo.prioridade})"
        return "Nenhum processo para executar"
    
    def modificar_prioridade(self, pid, nova_prioridade):
        if pid in self.processos:
            self.processos[pid].prioridade = nova_prioridade
            self.fila_prioridade = list(self.processos.values())
            heapq.heapify(self.fila_prioridade)

escalonador = Escalonador()
escalonador.adicionar_processo(1, 10, 3)
escalonador.adicionar_processo(2, 5, 1)
escalonador.adicionar_processo(3, 8, 2)

print(escalonador.executar_proximo())
escalonador.modificar_prioridade(3, 0)
print(escalonador.executar_proximo())
