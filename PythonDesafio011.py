# Faça um programa que lea a largura e a altura de uma parede em metros, 
# calcule a sua area e a quantidade de tinta necessaria para pintar, 
# sabendo que cada litro de tinta pinta uma area de 2m

larg = float(input("Largura da Parede: "))
alt = float(input("Altura da Parede: "))
área = larg * alt
print("Sua parede tem a dimensao de {}x{} e sua área é de {}m2".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, voce precisara de {}L de tinta".format(tinta))
