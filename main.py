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
os.system(
    'clear')  #MARK - Caso use windows troque a string por 'cls' ou 'CLEAR'


def adcionarDataDeTarefa():
    while True:
        dataAbertura = input(
            "Informe a data do início da atividade no formato DD/MM/AAAA: ")
        horaAbertura = input(
            "Informe a hora de início da atividade no formato HH:MM: ")

        try:
            data_hora = datetime.strptime(f"{dataAbertura} {horaAbertura}",
                                          "%d/%m/%Y %H:%M")
            return data_hora
        except ValueError:
            print(
                "Formato de data ou hora inválido. Por favor, insira novamente."
            )


verifica_cria_arquivo(nome_arquivo="atividades.txt")

usuario = Usuario("Usuario1", Agenda("atividades.txt"))
while True:
    print("=============================================")
    print("Escolha uma opção:")
    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefa")
    print("3 - Visualizar Tarefas")
    print("4 - Sair\n")

    opcao = int(input(">"))

    if opcao == 1:
        print("=============================================")
        nome = input("Qual o nome da atividade deseja adicionar: ")
        print("---------------------------------------------")
        opc_tipo = input(
            "Escolha o tipo da tarefa:\na - Profissional\nb - Pessoal:\n> "
        ).upper()
        while (opc_tipo != "A" and opc_tipo != "B"):
            print("---------------------------------------------")
            print("Opcao invalida, digite novamente")
            opc_tipo = input(
                "Escolha o tipo da tarefa:\na - Profissional\nb - Pessoal:\n> "
            ).upper()

        if (opc_tipo == "A"):
            tipo = "PROFISSIONAL"
        elif (opc_tipo == "B"):
            tipo = "PESSOAL"
        else:
            raise Exception("Erro na opcao escolhida")

        print("---------------------------------------------")

        dataHora = adcionarDataDeTarefa()
        print("---------------------------------------------")
        prazo = input(
            "Qual o tempo previsto de duração da atividade mais d para dia ou h para hora(Exemplo: 14d, 1h):"
        )
        
        usuario.adicionarTarefa(Atividade(nome, tipo, prazo, dataHora))
        usuario.mostraAtividade()
        print("=============================================")

        usuario.agenda.gravarAtividades(nome_arquivo="atividades.txt")

    elif opcao == 2:
        print("=============================================")
        usuario._agenda.mostraAtividade()
        opc_delete = int(input("Qual atividade deseja remover:")) - 1
        while(not usuario.removerTarefa(opc_delete)):
            opc_delete = int(input("Qual atividade deseja remover:")) - 1
        print("============================================")
        usuario.mostraAtividade()

    elif opcao == 3:
        print("=============================================")
        usuario.mostraAtividade()

    elif opcao == 4:
        print("=============================================")
        break
    else:
        print(
            f"\nNumero digitado e invalido por gentileza digite um novo numero\n"
        )
