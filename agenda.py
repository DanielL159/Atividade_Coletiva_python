class Agenda:
    
    def __init__(self):
        self._lista = []
        
    @property
    def lista(self):
        return self._lista
    
    def adicionarALista(self,tarefa):
        self.lista.append(tarefa)
        
    def __str__(self):
        return f"{self.lista}"
