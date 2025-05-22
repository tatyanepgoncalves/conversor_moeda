# The class `Conversor` in Python defines a currency converter that converts values from one currency
# to another based on provided exchange rates.
class Conversor: 
  # Cria objeto conversor de moedas
  def __init__(self, taxas_moedas: dict):
    self.taxas_moedas = taxas_moedas
  
  # Converte o valor de uma moeda para outra
  def converte_moeda(self, valor_moeda: float, moeda_inicial: str, moeda_final: str) -> float:
    moeda_inicial = moeda_inicial.upper()
    moeda_final = moeda_final.upper()

    # Caso de erro
    if moeda_inicial not in self.taxas_moedas or moeda_final not in self.taxas_moedas:
      raise ValueError("Moeda inválida!")
    
    valor_real = valor_moeda * self.taxas_moedas[moeda_inicial] # Converte para real
    valor_convertido = valor_real / self.taxas_moedas[moeda_final] # Converte para outra moeda

    return valor_convertido