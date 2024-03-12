#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo

from math import sin, radians, cos, tan
angulo = float(input("Digite o Angulo que voce deseja: "))
seno = sin(radians(angulo))
print("O Angulo de: {} tem o Seno de: {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O Angulo de: {} tem o Cosseno de: {:.2f}".format(angulo,cosseno))
tangente = tan(radians(angulo))
print("O Angulo de: {} tem a Tangente de: {:.2f}".format(angulo,tangente))
