from conversor import Conversor
from moeda import Moeda

# O coração da aplicação
def main():
  taxas = {
    "BRL": 1.0,
    "USD": 5.73,
    "EUR": 6.46,
    "JPY": 0.040,
    "GBP": 7.67
  }

  moedas = {
    "BRL": Moeda("BRL", "Real Brasileiro", "R$"),
    "USD": Moeda("USD", "Dólar Americano", "US$"),
    "EUR": Moeda("EUR", "Euro", "€"),
    "JPY": Moeda("JPY", "Iene Japonês", "¥"),
    "GBP": Moeda("GBP", "Libra Esterlina", "£"),
  }

  # Chama a class Conversor e exibe o resultado
  conversor = Conversor(taxas)

  try: 
    print("Bem-vindo ao MoneyGo 💸")
    print("Moedas disponíveis: BRL, USD, EUR, JPY")
    moeda_inicial = input("Converter DE (ex: USD): ").strip()
    moeda_final = input("Converter PARA (ex: BRL): ").strip()
    valor_moeda = float(input("Digite o valor a converter: "))

    resultado = conversor.converte_moeda(valor_moeda, moeda_inicial, moeda_final)
    print(f"\n{moedas[moeda_inicial].simbolo_moeda}{valor_moeda:.2f} equivale a {moedas[moeda_final].simbolo_moeda}{resultado:.2f}")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()