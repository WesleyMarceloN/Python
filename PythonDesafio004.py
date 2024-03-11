#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

texto001 = input("Digite Algo: ")
print("O Tipo Primitivo desse valor é: ", type(texto001))
print("Tem Espaços? ", texto001.isspace())
print("É um Numero? ", texto001.isnumeric())
print("É Alfabetico? ", texto001.isalpha())
print("É AlfaNumérico? ", texto001.isalnum())
print("Esta em Maiuscula? ", texto001.isupper())
print("Esta em Minuscula? ", texto001.islower())
print("Esta Captalizada? ", texto001.istitle())
