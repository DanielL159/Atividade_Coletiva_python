#Agenda de Tarefas Console: Desenvolva uma agenda de
#tarefas simples em que os usuários podem adicionar,
#remover e visualizar tarefas diretamente no terminal.
#Você pode usar um arquivo de texto para armazenar as tarefas localmente.

from agenda import Agenda
from usuario import Usuario
from atividade import Atividade

usuario = Usuario("Usuario1",Agenda())
while True:

    print("""
                                                1- ADICIONAR ATIVIDADE
                                                2- REMOVER ATIVIDADE
                                                3- VISUALIZAR ATIVIDADES
                                                4- SAIR
                                                O que desejar fazer:""",end=" ")
    opcao=int(input())
    
    if opcao == 1:
        nome= input("Qual atividade deseja adicionar:")
        tipo=input("Tipo de atividade(PROFISSIONAL)(PESSOAL):")
        
        while tipo.upper() != "PROFISSIONAL" and tipo.upper() != "PESSOAL":
            tipo=input("Tipo de atividade(PROFISSIONAL)(PESSOAL):")
            
        prazo=input("Qual o tempo previsto de duração da atividade:")
        usuario.adicionarTarefa(Atividade(nome,tipo,prazo))
        usuario.mostraAtividade()
        
    elif opcao == 2:
        nome= input("Qual atividade deseja remover:")
        usuario.removerTarefa(nome)
        usuario.mostraAtividade()
        
    elif opcao == 3:
        usuario.mostraAtividade()

    elif opcao == 4:
        break;
    else:
        print(f"\nNumero digitado e invalido por gentileza digite um novo numero\n")
