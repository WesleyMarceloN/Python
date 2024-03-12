#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porçao inteira
#exemplo: digite um numero: 6.127 o numero 6.127 tem a parte inteira 6
#dica: math

from math import floor, trunc
num = float(input("Digite Um Numero: "))
print("Numero Digitado foi: {}".format(num))
numint = float(floor(num))
print("O Numero: {} tem sua parte inteira: {}".format(num,numint))
print("O Numero: {} tem sua parte inteira: {}".format(num, trunc(num)))
print("O Numero: {} tem sua parte inteira: {:.0f}".format(num,num)) #nesse caso nao precisaria importar a biblioteca math
print("O Numero: {} tem sua parte inteira: {}".format(num, int(num))) #outro exemplo que nao precisaria importar o math
