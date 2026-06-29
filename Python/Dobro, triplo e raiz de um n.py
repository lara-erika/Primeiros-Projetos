#faça um programa que leia um número inteiro e mostre na tela o seu dobro, triplo e raiz quadrada#
n = int(input("Olá!\nDigite um número inteiro:"))
print("O número digitado foi: {}\nO seu dobro é: {}\nO seu triplo é: {}\nA sua raiz quadrada é: {:.2f}".format(n, n*2, n*3, n**(1/2)))
