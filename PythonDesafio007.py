#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

n1 = float(input("Digite sua Primeira Nota: "))
n2 = float(input("Digite sua Segunda Nota: "))
media = (n1 + n2) / 2
print("Sua Media é: {:.1f}".format(media))
