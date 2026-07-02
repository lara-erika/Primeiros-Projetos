#Este programa tem o objetivo de ler um valor em reais e converter para dólares, considerando a cotação do dólar fornecida pelo usuário.#
valor_reais = float(input("Digite o valor em reais: "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))
valor_dolares = valor_reais / cotacao_dolar
print("O valor em dólares é: ${:.2f}".format(valor_dolares))
continuar = input("Deseja realizar outra conversão? (s/n): ")
while continuar.lower() == 's':
    valor_reais = float(input("Digite o valor em reais: "))
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
    valor_dolares = valor_reais / cotacao_dolar
    print("O valor em dólares é: ${:.2f}".format(valor_dolares))
    continuar = input("Deseja realizar outra conversão? (s/n): ")