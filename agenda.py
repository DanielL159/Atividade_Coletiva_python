class Agenda:
    
    def __init__(self):
        self._lista = []
        
    @property
    def lista(self):
        return self._lista
    
    def adicionarALista(self,tarefa):
        self.lista.append(tarefa)
        
    def removerDaLista(self,contador):
        del self.lista[contador]
        
    def mostraAtividade(self):
        for atividade in self.lista:
            print("Nome:", atividade.nome)
            print("Tipo:", atividade.tipo)
            print("Prazo:", atividade.prazo)
            print()
            
