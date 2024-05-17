#Agenda de Tarefas Console: Desenvolva uma agenda de
#tarefas simples em que os usuários podem adicionar,
#remover e visualizar tarefas diretamente no terminal.
#Você pode usar um arquivo de texto para armazenar as tarefas localmente.

def verifica_cria_arquivo(nome_arquivo):
  if not os.path.exists(nome_arquivo):
    with open(nome_arquivo, "a") as arquivo:
        pass
    return False
  else:
    return True

from datetime import datetime, timedelta
import os

from agenda import Agenda
from usuario import Usuario
from atividade import Atividade

# Essa funcao limpa o terminal automaticamente
os.system('clear') #MARK - Caso use windows troque a string por 'cls' ou 'CLEAR'


def adcionarDataDeTarefa():
    while True:
        dataAbertura = input("Informe a data do início da atividade no formato DD/MM/AAAA: ")
        horaAbertura = input("Informe a hora de início da atividade no formato HH:MM: ")

        try:
            data_hora = datetime.strptime(f"{dataAbertura} {horaAbertura}", "%d/%m/%Y %H:%M")
            return data_hora
        except ValueError:
            print("Formato de data ou hora inválido. Por favor, insira novamente.")

verifica_cria_arquivo(nome_arquivo="atividades.txt")

usuario = Usuario("Usuario1",Agenda("atividades.txt"))
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

        dataHora = adcionarDataDeTarefa()
        prazo= input("Qual o tempo previsto de duração da atividade mais d para dia ou h para hora:")

        usuario.adicionarTarefa(Atividade(nome,tipo,prazo,dataHora))
        print(f"\n")
        print(usuario)
        usuario.mostraAtividade()
        #print(usuario)
        usuario.agenda.gravarAtividades(nome_arquivo="atividades.txt")


    elif opcao == 2:
        nome= input("Qual atividade deseja remover:")
        usuario.removerTarefa(nome)
        usuario.mostraAtividade()

    elif opcao == 3:
      print(f"\n")
      print(usuario)
      usuario.mostraAtividade()
  

    elif opcao == 4:
        break;
    else:
        print(f"\nNumero digitado e invalido por gentileza digite um novo numero\n")
