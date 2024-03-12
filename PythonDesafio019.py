#Um professor quer sortear um dos seus quatro aluno para apagar o quadro. faça um programa que ajude ele lendo o nome deles e escrevendo o nome escolhido

from random import choice
n1 = str(input("Primeiro Aluno: "))
n2 = str(input("Segundo Aluno: "))
n3 = str(input("Terceiro Aluno: "))
n4 = str(input("Quarto Aluno: "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O Aluno escolhido foi: {}".format(escolhido))
