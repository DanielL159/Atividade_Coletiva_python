import time 

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
            print()
            print("Nome:", atividade.nome)
            print("Tipo:", atividade.tipo)
            print("Prazo:", atividade.prazo)
            print("Horário de inicio da atividade:", atividade.dataAbertura.strftime("%d/%m/%Y %H:%M:%S"))
            print("Horário do fim da Atividade:", atividade.dataFim.strftime("%d/%m/%Y %H:%M:%S"))
            print()

         
