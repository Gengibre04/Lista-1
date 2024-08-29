#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a
#mensagem "Bom Dia!", "Boa Tarde!"" ou "Boa Noite!"" ou "Valor Inválido!", conforme o caso
Horário = input("Em que turno você estuda? Digite M para matutino, V para vespertino e N para noturno!\n")
if Horário == "m" or Horário == "M":
    print("Matutino") 
    print("Bom dia!")
elif Horário == "v" or Horário == "V":
    print("Vespertino")
    print("Boa tarde!")
elif Horário == "n" or Horário == "N":
    print("Noturno")
    print("Boa noite!")
else: 
    print("Valor inválido")