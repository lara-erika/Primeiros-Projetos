#Este programa tem o objetivo de ler um valor em metros e conevertê-lo para centímetros e milímetros.#
valor_metros = float(input("Digite um valor em metros: "))
valor_centimetros = valor_metros * 100
valor_milimetros = valor_metros * 1000
print("O valor digitado foi: {:.2f} metros\nO valor em centímetros é: {:.2f} cm\nO valor em milímetros é: {:.2f} mm".format(valor_metros, valor_centimetros, valor_milimetros))