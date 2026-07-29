#Um professor quer sortear a ordem de apresentação dos seus quatro alunos. Faça um programa que ajude ele, lendo o nome deles e escrevendo a ordem sorteada.#
from random import shuffle
n1 = str(input('Qual o nome do primeiro aluno?\n'))
n2 = str(input('Qual o nome do segundo aluno?\n'))
n3 = str(input('Qual o nome do terceiro aluno?\n'))
n4 = str(input('Qual o nome do quarto aluno?\n'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print('\n'.join(lista))
