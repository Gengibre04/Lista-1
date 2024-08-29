#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
try:
    Letra = input("Digite a Letra\n")
    if Letra == "a" or Letra == "e" or Letra == "i" or Letra == "o" or Letra == "u":
        print("Vogal")
    else:
        print("consoante\n")
except ValueError:
    print("Está sem letras\n")