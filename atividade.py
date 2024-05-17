import time
from datetime import datetime, timedelta


class Atividade:
    __slots__ = ['_nome', '_tipo', '_prazo', '_dataAbertura', '_dataFim']

    def __init__(self, nome, tipo, prazo, dataAbertura):
        self._nome = nome
        self._tipo = tipo
        self._prazo = prazo
        self._dataAbertura = dataAbertura
        self._dataFim = self.calculaPrazoFinal()

    @property
    def prazo(self):
        return self._prazo.upper()

    @property
    def nome(self):
        return self._nome.upper()

    @property
    def tipo(self):
        return self._tipo.upper()

    @property
    def dataAbertura(self):
        return self._dataAbertura

    @property
    def dataFim(self):
        return self._dataFim

    def calculaPrazoFinal(self):
        if self.prazo[1] == 'D':
            return self.dataAbertura + timedelta(days=int(self.prazo[0]))
        elif self.prazo[1] == 'H':
            return self.dataAbertura + timedelta(hours=int(self.prazo[0]))
 
    def __str__(self):
        return f"NOME:{self.nome}\nTIPO:{self.tipo}\nDATA DE INICIO:{self.dataAbertura}\nDATA DE ENCERRAMENTO:{self.dataFim}"