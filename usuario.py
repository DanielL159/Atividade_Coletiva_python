class Usuario:
  __slots__ = ['_nome', '_agenda']
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

  def removerTarefa(self,posicao):
    return self.agenda.removerDaLista(posicao)


  def mostraAtividade(self):
      self.agenda.mostraAtividade()


  def __str__(self):
      return f"{self.nome} :\n {self.agenda}"
