#O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos, faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada

from random import shuffle
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação sera: ")
print(lista)
