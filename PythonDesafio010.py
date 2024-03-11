#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# 33:10
real = float(input("Quantos dinheiro vc tem? R$ "))
#dolar = real / 3.27
#print("O valor que voce tem na sua carteira é de {} reais, convertido para o dolar que esta {} dollar hoje, voce tem o equivalente a {} dolares convertido".format(valorreal,valordolares,valorconvertido))
print("-" * 40)
print("Com R$ {} Voce consegue converter em".format(real))
print("-" * 40)
print("US$ {:.2f}".format(real / 4.90))
print("EUR$ {:.2f}".format(real / 5.31))
print("GBP$ {:.2f}".format(real / 6.07))
print("JPY$ {:.2f}".format(real / 0.03))
