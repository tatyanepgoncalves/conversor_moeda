class Moeda:
  # Cria objeto de moeda
  def __init__(self, codigo_moeda: str, nome_moeda: str, simbolo_moeda: str):
   self.codigo_moeda = codigo_moeda.upper()
   self.nome_moeda = nome_moeda
   self.simbolo_moeda = simbolo_moeda


  # Mostra uma string quando executado
  def __str__(self):
    return f"{self.nome_moeda} ({self.codigo_moeda} - {self.simbolo_moeda})"