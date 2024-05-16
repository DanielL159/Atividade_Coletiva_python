class Atividade:
    
    def __init__(self,nome,tipo,prazo):
        self._nome = nome
        self._tipo = tipo
        self._prazo = prazo
        
    @property
    def prazo(self):
        return self._prazo
    
    @property
    def nome(self):
        return self._nome.upper()
    
    @property
    def tipo(self):
        return self._tipo.upper()

  
        
    
