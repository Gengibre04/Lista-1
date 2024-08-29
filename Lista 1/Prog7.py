#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
#pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
#"Assassino". Caso contrário, ele será classificado como "Inocente".

score = 0

print("Vamos saber seu envolvimento com a vítima\n")
print("responda as seguintes perguntas com S ou N\n")

def ask_pergunta(pergunta):
    while True:
        resposta = input(pergunta + " (S/N): ").upper()
        if resposta in ['S', 'N']:
            return resposta
        else:
            print("Resposta inválida")

# Questao 1
resposta = ask_pergunta("Telefonou para a vítima?\n")
if resposta == 'S':
    score += 1 

# Questao 2
resposta = ask_pergunta("esteve no local do crime?\n")
if resposta == 'S':
    score += 1  

# Questao 3
resposta = ask_pergunta("Mora perto da vítima?\n")
if resposta == 'S':
    score += 1  

# Questao 4
resposta = ask_pergunta("Devia para a vítima?\n")
if resposta == 'S':
    score += 1 

# Questao 5
resposta = ask_pergunta("ja trabalhou com a vítima?\n")
if resposta == 'S':
    score += 1 

if score == 5:
    print("Assassino!")
elif score >= 4 or score == 3:
    print("cúmplice")
elif score == 2:
    print("Suspeito")
else:
    print("inocente")


print(f"culpometro marcou: {score}")