#Este program tem como objetivo ler um número real e mostrar na tela sua porção inteira.
from math import trunc

n = float(input("Digite um número real: "))
print("A porção inteira do número digitado é: {}".format(trunc(n)))
