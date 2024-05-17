import time
from datetime import datetime

from atividade import Atividade


def le_linha_csv(linha):
    info_linha = []
    info_linha = linha.split(',')
    last_idx = len(info_linha) - 1
    info_linha[last_idx] = info_linha[last_idx].replace('\n', '')
    return info_linha


class Agenda:
    __slots__ = ['_lista', '_arquivo']

    def __init__(self, arquivo):
        self._lista = []
        self._arquivo = arquivo
        self.start()

    @property
    def lista(self):
        return self._lista

    def adicionarALista(self, tarefa):
        self.lista.append(tarefa)
        self.gravarAtividades(self._arquivo)

    def removerDaLista(self, contador):
        del self.lista[contador]
        self.gravarAtividades(self._arquivo)

    def mostraAtividade(self):
        for atividade in self.lista:
            print("Nome:", atividade.nome)
            print("Tipo:", atividade.tipo)
            print("Prazo:", atividade.prazo)
            print("Horário de inicio da atividade:",
                  atividade.dataAbertura.strftime("%d/%m/%Y %H:%M:%S"))
            print("Horário do fim da Atividade:",
                  atividade.dataFim.strftime("%d/%m/%Y %H:%M:%S"))
            print()

    def gravarAtividades(self, nome_arquivo):
        with open(nome_arquivo, "w") as arquivo:
            for atividade in self.lista:
                arquivo.write(
                    f"{atividade.nome},{atividade.tipo},{atividade.prazo},{atividade.dataAbertura.strftime('%d/%m/%Y %H:%M:%S')},{atividade.dataFim.strftime('%d/%m/%Y %H:%M:%S')}\n"
                )

    def start(self):
        with open(self._arquivo, "r") as arquivo:
            csv = arquivo.readlines()
            n_linhas = len(csv)
        for i in range(n_linhas):
            dados_linha_atual = le_linha_csv(csv[i])
            atividade_atual = Atividade(
                dados_linha_atual[0], dados_linha_atual[1],
                dados_linha_atual[2],
                datetime.strptime(dados_linha_atual[3], "%d/%m/%Y %H:%M:%S"))
            self._lista.append(atividade_atual)
