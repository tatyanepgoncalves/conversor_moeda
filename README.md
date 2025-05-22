# 🪙 Conversor de Moeda - MoneyGo

## 🔥 Introdução
O MoneyGo é uma aplicação back-end simples que converte valores entre diferentes moedas (real para dólar, euro...). O foco é praticar conceitos de Python com **Programação Orientada a Objetos**.

---

## ✨ Funcionalidades
- **Entrada de dados do usuário**: valor, moeda de origem e moeda de destino.
- **Validação de entrada**: impedir valores inválidos (letras, valores negativos, moedas inexistentes).
- **Conversão de moeda**: cálculo com base na taxa de câmbio.
- **Exibição do resultado**: mostrar valor convertido.

---
## 🧠 Conceitos aplicados

- Python 3
- Programação Orientada a Objetos (POO)
- Modularização
- Tratamento de erros
- Entrada de dados via terminal

---
## 🗂️ Estrutura dos Arquivos

```bash
conversor_moeda/
├── main.py         # Ponto de entrada do programa
├── LICENSE         # Licença do programa
├── conversor.py    # Contém a lógica da conversão
├── moeda.py        # Representa as moedas disponíveis
└── README.md       # Documentação da aplicação
```
---

## 🧾 Como usar
### ✅ Pré-requisitos
- `Python 3.7` ou superior instalado

## 🚀 Executar o projeto

1 - Clone o repositóripo ou baixe os arquivos:
```bash
git clone https://github.com/tatyanepgoncalves/conversor_moeda.git
cd conversor_moeda
```

2 . Rode o programa
```bash
python main.py
```

3. Siga as instruções no terminal e converta à vontade! 

---
## 💡 Exemplo de uso

```py
Bem-vindo ao MoneyGo 💸
Moedas disponíveis: BRL, USD, EUR, JPY
Converter DE (ex: USD): USD
Converter PARA (ex: BRL): EUR
Digite o valor a converter: 10

US$10.00 equivale a €8.87

```

---

## 🛠️ Tecnologias usadas
- Python 3
- Terminal/CLI

---
## 📌 Possíveis melhorias futuras
- Integração com API real de câmbio (ex: [ExchangeRate API](https://www.exchangerate-api.com/))
- Interface gráfica com **Tkinter** ou **PyQt**
- Exportar histórico para `.json` ou `.csv`
- Testes automatizados com `unittest` ou `pytest`


---
## ✍️ Autoria

Projeto desenvolvido por Tatyane Gonçalves, estudante de Sistemas de Informação, focada em full stack e com sede de aprender.

---

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, estudar e melhorar!