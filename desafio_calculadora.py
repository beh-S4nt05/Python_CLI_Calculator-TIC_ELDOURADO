'''
- Desafio: Calculadora Simples.
- Requisitos Técnicos: Laços de repetição, condicionais, entrada e saída de dados, operações matemáticas, coleções de dados.
- Descrição Geral: Desenvolva um aplicativo de calculadora que funcione bia linha de comando (terminal).

O usuário deve ser capaz de escolher entre diferentes operações matemáticas, inserir números para realizar os cálculos, e navegar no menu do aplicativo.

Requisitos Funcionais:
Menu Principal:

Calculadora Simples:

1. Soma
2. Subtração
3. Multiplicação
4. Divisão
s. Sair

Deve escolher a operação utilizando os números referentes à opção do menu e apertar ENTER.
Uma vez escolhida a operação, a aplicação deverá solicitar dois números e executar a operação selecionada sobre eles.
IMPORTANTE!! Precisamos nos atentar às divisões por zero!

Entrada:
"Primeiro número:"
"Segundo número:"

Saída:
O Resultado da [OPERAÇÃO SELECIONADA] é: [RESULTADO]
Ex.: "O resultado da operação soma é: 42"

Quando a operação for finalizada, deverá voltar ao menu principal.
Se o usuário escolher a opção s, o aplicativo deverá agradecer o usuário e sair.
'''

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
    os.system("cls")

  def operacoes(self):
    opcao = input("Escolha uma opção ou 's' para sair: ")
    os.system("cls")
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