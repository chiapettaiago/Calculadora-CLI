print('Calculadora de linha de comando versão 1.0')
operacao = input('Soma, multiplicação, subtração ou divisão? ')

numero1 = input('Digite o primeiro número  ')
numero2 = input('Digite o segundo número   ')

if(operacao == "soma"):
  resultado = int(numero1) + int(numero2)
elif (operacao == "subtração"):
  resultado = int(numero1) - int(numero2)
elif (operacao == "multiplicação"):
  resultado = int(numero1) * int(numero2)
elif (operacao == "divisão"):
  resultado = int(numero1) / int(numero2)
else:
  resultado = "Operação não suportada"



print('O resultado da operação é ', str(resultado))