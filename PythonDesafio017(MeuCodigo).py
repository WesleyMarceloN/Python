#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da sua hipotenusa

print("Vamos Descobri a Hipotenusa de um triangulo retangulo")
ca = float(input("Cateto Oposto: "))
co = float(input("Cateto Adjacente: "))
somacat = (ca**2 + co**2)
print("Hipotenusa: {}/2".format(somacat))
print("Hipotenusa: {:.2f}".format(somacat**(1/2)))

# versao com import

from math import hypot
hi = hypot(co, ca)
print("A Hipotenusa vai Medir: {:.2f}".format(hi))
