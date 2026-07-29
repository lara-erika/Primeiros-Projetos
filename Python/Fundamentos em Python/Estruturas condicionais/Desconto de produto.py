#Este programa calcula o desconto de um produto com base em uma porcentagem fornecida pelo usuário.#
preco = float(input("Digite o preço do produto: \n"))
percentual_desconto = float(input("Digite o percentual de desconto: \n"))
desconto = preco * (percentual_desconto / 100)
preco_final = preco - desconto
print("O desconto é: R$ {:.2f}".format(desconto))
print("O preço final é: R$ {:.2f}".format(preco_final)) 
while True:
    resposta = input("Deseja calcular o desconto de outro produto? (s/n): ")
    if resposta.lower() == 's':
        preco = float(input("Digite o preço do produto: \n"))
        percentual_desconto = float(input("Digite o percentual de desconto: \n"))
        desconto = preco * (percentual_desconto / 100)
        preco_final = preco - desconto
        print("O desconto é: R$ {:.2f}".format(desconto))
        print("O preço final é: R$ {:.2f}".format(preco_final)) 
    elif resposta.lower() == 'n':
        print("Obrigado por usar o programa!")
        break
    else:
        print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")