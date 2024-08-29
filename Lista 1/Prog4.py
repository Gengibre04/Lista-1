#Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:
#a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#b. A mensagem "Reprovado", se a média for menor do que sete;
#c. A mensagem "Aprovado com Distinção", se a média for igual a dez
try:
    Nota1 = float(input("Digite a primeira nota da prova\n")) 
    Nota2 = float(input("Digite a segunda nota da prova\n"))
    Media = (Nota1 + Nota2) / 2
    if Media == 10:
        print("Aprovado com distinção")
    elif Media < 7:
        print("reprovado")
    elif Media >= 7:
        print("Aprovado")
except ValueError:
    print("Isso é uma letra")
            
            
            


