#Crie um programa que leia o valor de um produto e mostra o pagamento a vista com 10% de desconto ou parcelado com 8% de aumento

produto = float(input("Nos Informe o Valor do produto: R$"))
produtodesc = produto - (produto * 10 / 100)
produto1x = produto + (produto * 8 / 100)
print("=" * 20)
print("Valor: R${}".format(produto))
print("=" * 20)
print("A Vista: R${}".format(produtodesc))
print("=" * 20)
print("Parcelado")
print("1x R${}".format(produto1x))
print("=" * 20)
