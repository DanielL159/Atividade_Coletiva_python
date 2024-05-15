#Agenda de Tarefas Console: Desenvolva uma agenda de
#tarefas simples em que os usuários podem adicionar,
#remover e visualizar tarefas diretamente no terminal.
#Você pode usar um arquivo de texto para armazenar as tarefas localmente.

from agenda import Agenda
from usuario import Usuario

tarefa = str(input("Tarefa:"))
usuario = Usuario("Jorge" , Agenda())

usuario.adicionarTarefa(tarefa)

print(usuario)
