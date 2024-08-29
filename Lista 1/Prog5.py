#Faça um Programa que leia três números e mostre o maior deles
try:
    num1 = int(input("Digite um número\n"))
    num2 = int(input("Digite um número\n"))
    num3 = int(input("Digite um número\n"))
    if num1 > num2 and num1 > num3:
        print("Primeiro número é maior")
    elif num2 > num3 and num2 > num1:
        print("Segundo número é maior") 
    else:
        print("Terceiro número é maior")
except ValueError:
    print("DIGITE UM NÚMERO!!!\n")