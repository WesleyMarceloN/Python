#Escreva um Programa que leia um valor em metros e converte ele em centimetros e em milimetros

tamanhom = float(input("Escreva Um Valor em Metros: "))
tamquil = tamanhom / 1000
tamhect = tamanhom / 100
tamdeca = tamanhom / 10
tamdeci = tamanhom * 10
tamcent = tamanhom * 100
tammili = tamanhom * 1000
print("{} Metros Digitado".format(tamanhom))
print("{} Quilometro".format(tamquil))
print("{} Hectometro".format(tamhect))
print("{} Decatro".format(tamdeca))
print("{} Decimetro".format(tamdeci))
print("{} Centimetro".format(tamcent))
print("{} Milimetro".format(tammili))
