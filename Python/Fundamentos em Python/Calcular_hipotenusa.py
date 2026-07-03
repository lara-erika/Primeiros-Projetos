#Este programa tem como ojetivo calcular a hipotenusa, ou cateto adjacente, ou cateto oposto, de um triângulo retângulo, utilizando o teorema de Pitágoras.#
import math

print("Bem-vindo ao programa de cálculo do teorema de Pitágoras!\n")
cateto_oposto = input("Digite o valor do cateto oposto (ou pressione Enter para pular): ")
cateto_adjacente = input("Digite o valor do cateto adjacente (ou pressione Enter para pular): ")
hipotenusa = input("Digite o valor da hipotenusa (ou pressione Enter para pular): ")

if cateto_oposto and cateto_adjacente: #Para descobrir hipotenusa#
    cateto_oposto = float(cateto_oposto)
    cateto_adjacente = float(cateto_adjacente)
    hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
    print("O valor da hipotenusa é: {:.2f}".format(hipotenusa))

elif cateto_oposto and hipotenusa: # Para descobrir o cateto adjacente
    cateto_oposto = float(cateto_oposto)
    hipotenusa = float(hipotenusa)

    if hipotenusa <= cateto_oposto:
        print("Erro: a hipotenusa deve ser maior que o cateto oposto.")
    else:
        cateto_adjacente = math.sqrt(hipotenusa**2 - cateto_oposto**2)
        print("O valor do cateto adjacente é: {:.2f}".format(cateto_adjacente))

elif cateto_adjacente and hipotenusa: # Para descobrir o cateto oposto
    cateto_adjacente = float(cateto_adjacente)
    hipotenusa = float(hipotenusa)

    if hipotenusa <= cateto_adjacente:
        print("Erro: a hipotenusa deve ser maior que o cateto adjacente.")
    else:
        cateto_oposto = math.sqrt(hipotenusa**2 - cateto_adjacente**2)
        print("O valor do cateto oposto é: {:.2f}".format(cateto_oposto))
else: 
    print("Erro: você deve fornecer pelo menos dois valores para calcular o terceiro.")
