#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. 
# Dica: utilize o operador módulo (resto da divisão[%]).
try:
    numero = int(input("Digite um numero:\n"))
    if numero % 2 == 0:
        print("Par")
    elif int(numero) % 2 != 0:
        print("impar")
except ValueError:
    print("Numero não numerico!\n")