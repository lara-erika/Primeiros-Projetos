#Este program exibe a tabuada de um número inteiro fornecido pelo usuário.#
num = int(input("Digite um número inteiro para ver sua tabuada: "))
print("Tabuada do número {}:".format(num))
for i in range(1, 11):
    resultado = num * i
    print("{} x {} = {}".format(num, i, resultado))
