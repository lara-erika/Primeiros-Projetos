#Este código tem como objetivo ser um contador inteligente que permite ao usuário definir o início, o fim e o passo da contagem. O programa exibirá a contagem de acordo com os parâmetros fornecidos.
print("Bem-vindo ao contador inteligente!\n")
início = int(input("Digite o início da contagem: "))
fim = int(input("Digite o fim da contagem: "))
passo = int(input("Digite o passo da contagem: "))
print("Contagem de {} até {} com passo {}:".format(início, fim, passo))
if início < fim:
    for i in range(início, fim + 1, passo):
        print(i, end=' ')
elif início > fim:
    for i in range(início, fim - 1, -passo):
        print(i, end=' ')
else:
    print("O início e o fim da contagem são iguais. Não há contagem a ser feita.")
continuar = input("\nDeseja realizar outra contagem? (s/n): ")
while continuar.lower() == 's':
    início = int(input("Digite o início da contagem: "))
    fim = int(input("Digite o fim da contagem: "))
    passo = int(input("Digite o passo da contagem: "))
    print("Contagem de {} até {} com passo {}:".format(início, fim, passo))
    if início < fim:
        for i in range(início, fim + 1, passo):
            print(i, end=' ')
    elif início > fim:
        for i in range(início, fim - 1, -passo):
            print(i, end=' ')
    else:
        print("O início e o fim da contagem são iguais. Não há contagem a ser feita.")
    continuar = input("\nDeseja realizar outra contagem? (s/n): ")
if continuar == 'n':
        print("Obrigado por usar o contador inteligente!")
elif continuar != 's' and continuar != 'n':
        tentativa_2 = input("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")
        if tentativa_2 == 's':
            início = int(input("Digite o início da contagem: "))
            fim = int(input("Digite o fim da contagem: "))
            passo = int(input("Digite o passo da contagem: "))
            print("Contagem de {} até {} com passo {}:".format(início, fim, passo))
            if início < fim:
                for i in range(início, fim + 1, passo):
                    print(i, end=' ')
            elif início > fim:
                for i in range(início, fim - 1, -passo):
                    print(i, end=' ')
            else:
                print("O início e o fim da contagem são iguais. Não há contagem a ser feita.")
        elif tentativa_2 == 'n':
            print("Obrigado por usar o contador inteligente!")
