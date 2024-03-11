#Crie um algoritmo que leia um numero e mostre o seu dobra, triplo e raiz quadrada

num01 = int(input("Digite um Numero: "))
numdob = num01 * 2
numtri = num01 * 3
numrzq = num01 **(1/2)
print("O Numero escolhido foi {}".format(num01))
print("O Dobro do numero escolhido é: {}".format(numdob))
print("O Triplo do numero escolhido é: {}".format(numtri))
print("E a Raiz Quadrada do numero escolhido é: {}".format(numrzq))
