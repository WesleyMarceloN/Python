'''
Escreva um programa que pergunte a quantidade de km percorrido
por um carro alugado e a quantidade de dias pelo quais ele foi 
alugado. Calcule o preço a pagar, sabendo que o carro custa 
R$60 por dia e R$0.15 por Km rodado 
'''
dias = int(input("Quantos Dias Alugados? "))
km = float(input("Quantos Km Rodados? "))
pago = (dias * 60) + (km * 0.15)   
print("O Total a pagar é de R${:.2f}".format(pago))