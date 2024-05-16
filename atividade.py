import time
from datetime import datetime, timedelta

class Atividade:
    
    def __init__(self, nome, tipo, prazo, dataAbertura):
        self._nome = nome
        self._tipo = tipo
        self._prazo = int(prazo)
        self._dataAbertura = dataAbertura
        self._dataFim = self._dataAbertura + timedelta(days=self._prazo)

    @property
    def prazo(self):
        return self._prazo
    
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