# -*- coding: utf-8 -*-

print ("Para soma digite:          1")
print ("Para divisão digite:       2")
print ("Para multiplicação digite: 3")
print ("Para subtração digite:     4")

Operacao = input('Digite a operação desejada entre dois números inteiros:')

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if Operacao == "1":
  print ('O resultado é:',(valor1 + valor2))
elif Operacao == "2":
  print ('O resultado é:', (valor1 / valor2))
elif Operacao == "3":
  print ('O resultado é:', (valor1 * valor2))
elif Operacao == "4":
  print ('O resultado é:', (valor1 - valor2))
