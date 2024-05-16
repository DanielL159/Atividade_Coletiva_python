class Usuario:

    def __init__(self,nome,agenda):
        self._nome = nome
        self._agenda=agenda
        
    @property   
    def nome(self):
        return self._nome

    @property
    def agenda(self):
        return self._agenda
    
    def adicionarTarefa(self,tarefa):
        self.agenda.adicionarALista(tarefa)
        
    def removerTarefa(self,nome):
        posicao=-1
        for variavel in self.agenda.lista:
            posicao+=1
            if variavel.nome == nome.upper():
                self.agenda.removerDaLista(posicao)
                break;
        
    def mostraAtividade(self):
        self.agenda.mostraAtividade()


    def __str__(self):
        return f"{self.nome} :\n {self.agenda}"
