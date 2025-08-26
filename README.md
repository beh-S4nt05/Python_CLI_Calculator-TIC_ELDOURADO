# Calculadora Simples em Python

Trata-se de um projeto do desenvolvimento de uma calculadora funcional via (CLI) linha de comando - (terminal) utilizando Python. 
O objetivo é proporcionar uma experiência interativa e eficiente para realizar operações matemáticas básicas.

## 🚀 Desafio

Criar uma calculadora robusta que permita ao usuário realizar operações matemáticas fundamentais, com uma interface intuitiva e amigável no terminal. 
O foco está na clareza do código e na experiência do usuário.

## 🛠️ Requisitos Técnicos

*   **Laços de Repetição**: Utilização de `while` para manter o fluxo do programa.
*   **Condicionais**: Implementação de `if`, `elif`, e `else` para o controle de fluxo e seleção de operações.
*   **Entrada e Saída de Dados**: Uso de `input()` para capturar dados do usuário e `print()` para exibir resultados e mensagens.
*   **Operações Matemáticas**: Suporte para as operações básicas: Soma (+), Subtração (-), Multiplicação (*), e Divisão (/).
*   **Coleções de Dados**: Utilização de listas para gerenciar os tipos de operações disponíveis.
*   **Tratamento de Erros**: Mecanismos para lidar com situações como divisão por zero, garantindo a estabilidade do programa.

## 📝 Descrição Geral - Step by Step

O aplicativo da calculadora, desenvolvido em Python, oferece uma interface de menu simples para o usuário escolher entre as operações matemáticas disponíveis: Soma, Subtração, Multiplicação e Divisão. 
Após a seleção da operação, o usuário é solicitado a inserir dois números. 
A calculadora realiza o cálculo e exibe o resultado, retornando ao menu principal. 
Uma opção de saída permite ao usuário encerrar o programa de forma elegante.

## 📋 Requisitos Funcionais Detalhados

### 1. Menu Principal

O menu principal apresenta as seguintes opções:

```
Calculadora Simples:

	1. Soma
	2. Subtração
	3. Multiplicação
	4. Divisão
	s. Sair
```

*   O usuário deve selecionar uma operação digitando o número correspondente e pressionando ENTER.
*   Após a escolha, a aplicação solicitará dois números para realizar o cálculo.
*   **Importante**: O sistema deve tratar corretamente as divisões por zero, exibindo uma mensagem informativa e retornando ao menu.

### 2. Entrada de Dados

O programa solicitará os números da seguinte forma:

```
	Primeiro número: [seu número]
	Segundo número: [seu número]
```

* Exemplo:
```
  Primeiro número: 25
  Segundo número: 12
``` 

### 3. Saída de Dados

Os resultados serão exibidos de maneira clara e informativa:

```
O Resultado da [OPERAÇÃO SELECIONADA] é: [RESULTADO]
```

*   Exemplo: `O resultado da operação soma é: 37`

*   Após a conclusão de uma operação, o programa deve retornar ao menu principal, convidando o usuário a realizar outra operação.

*   Ao escolher a opção 's' (ou 'S'), o programa deve exibir uma mensagem de agradecimento e encerrar sua execução de maneira graciosa.

## 💻 Código Fonte (Exemplo)

```python
import os

class calculadora:
  def __init__(self):
    self.__numero1 = 0
    self.__numero2 = 0
    self.__resultado = 0
    self.__operacoesTipes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
    self.sair = False

  def entradas(self):
    self.__numero1 = float(input(f"\tPrimeiro Número: "))
    self.__numero2 = float(input(f"\tSegundo Número: "))

  def voltaraoMenu(self):
    input("\nPressione ENTER para voltar ao menu principal...")
    os.system("cls") # Use 'clear' no Linux/macOS

  def operacoes(self):
    opcao = input("Escolha uma opção ou 's' para sair: ")
    os.system("cls") # Use 'clear' no Linux/macOS
    if opcao not in ["1", "2", "3", "4", "s", "S"]:
      print("Opção inválida! Por favor escolha uma opção válida.")
      self.voltaraoMenu()
    elif opcao == "1":
      self.cabecalho_operacao(1)
      self.entradas()
      self.somar()
      self.mostrarResultado(1)
      self.voltaraoMenu()
    elif opcao == "2":
      self.cabecalho_operacao(2)
      self.entradas()
      self.subtrair()
      self.mostrarResultado(2)
      self.voltaraoMenu()
    elif opcao == "3":
      self.cabecalho_operacao(3)
      self.entradas()
      self.multiplicar()
      self.mostrarResultado(3)
      self.voltaraoMenu()
    elif opcao == "4":
      self.cabecalho_operacao(4)
      self.entradas()
      self.dividir()
      self.mostrarResultado(4)
      self.voltaraoMenu()
    else:
      self.powerOff()

  def somar(self):
    self.__resultado = self.__numero1 + self.__numero2

  def subtrair(self):
    self.__resultado = self.__numero1 - self.__numero2

  def multiplicar(self):
    self.__resultado = self.__numero1 * self.__numero2

  def dividir(self):
    if self.__numero2 == 0:
      print("Divisões por zero não são possíveis! Tente novamente.")
      self.entradas()
    else:
      self.__resultado = self.__numero1 / self.__numero2

  def agradecimento(self):
    print("\nObrigado por utilizar nossa calculadora!\nFeito com amor por Breno Santos")

  def powerOff(self):
    self.agradecimento()
    self.sair = True

  def mostrarResultado(self, opcao):
    print(f"\nO resultado da operação {self.__operacoesTipes[opcao-1]} é: {self.__resultado}")

  def cabecalho_operacao(self, opcao):
    print(f"> Calculadora Simples\n- Operação {self.__operacoesTipes[opcao-1]}:\n")

  def menu(self):
    print("\nCalculadora Simples: \n\n\t1. Soma\n\t2. Subtracao\n\t3. Multiplicacao\n\t4. Divisao\n\ts. Sair\n")
    self.operacoes()

calculadora = calculadora()

while calculadora.sair == False:
  calculadora.menu()
```

## 🚀 Como Executar

1.  Salve o código acima em um arquivo chamado `desafio_calculadora.py`.
2.  Abra o terminal ou prompt de comando.
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Execute o script com o comando: `python desafio_calculadora.py` ou `py desafio_calculadora.py`

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para aprimorar este projeto.
