#Este programa consiste em ler um número inteiro e exibir o seu dobro, seu triplo e sua raíz quadrada.
n = int(input("Olá!\nDigite um número inteiro:"))
print("O número digitado foi: {}\nO seu dobro é: {}\nO seu triplo é: {}\nA sua raiz quadrada é: {:.2f}".format(n, n*2, n*3, n**(1/2)))
