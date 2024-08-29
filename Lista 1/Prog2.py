#faça um programa que peça dois números e imprima o maior deles
try:
    num1 = int(input("Digite o primeiro número\n"))
    num2 = int(input("Digite o segundo número\n"))
    if num1 > num2:
        print(f"O primeiro numero é maior: {num1}")
    elif num1 < num2:
            print(f"O segundo numero é maior: {num2}")
except ValueError:
    print("Está sem número!\n")             