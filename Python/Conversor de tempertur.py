#Esse código tem como objetivo converter temperaturas entre Celsius, Fahrenheit e Kelvin. O usuário pode escolher a unidade de entrada e a unidade de saída desejada, e o programa realizará a conversão correspondente.#
print("Bem-vindo ao conversor de temperaturas!\n")
temp_inicial = float(input("Digite a temperatura que deseja converter (somente números): \n"))
unidade_entrada = int(input("Escolha a unidade de temperatura de entrada (1. Celsius, 2. Fahrenheit, 3. Kelvin): \n"))
unidade_saida = int(input("Escolha a unidade de temperatura de saída (1. Celsius, 2. Fahrenheit, 3. Kelvin): \n"))
if unidade_entrada == 1:  # Celsius
    if unidade_saida == 1:  # Celsius
        temp_final = temp_inicial
    elif unidade_saida == 2:  # Fahrenheit
        temp_final = (temp_inicial * 9/5) + 32
    elif unidade_saida == 3:  # Kelvin
        temp_final = temp_inicial + 273.15
elif unidade_entrada == 2:  # Fahrenheit
    if unidade_saida == 1:  # Celsius
        temp_final = (temp_inicial - 32) * 5/9
    elif unidade_saida == 2:  # Fahrenheit
        temp_final = temp_inicial
    elif unidade_saida == 3:  # Kelvin
        temp_final = (temp_inicial - 32) * 5/9 + 273.15
elif unidade_entrada == 3:  # Kelvin
    if unidade_saida == 1:  # Celsius
        temp_final = temp_inicial - 273.15
    elif unidade_saida == 2:  # Fahrenheit
        temp_final = (temp_inicial - 273.15) * 9/5 + 32
    elif unidade_saida == 3:  # Kelvin
        temp_final = temp_inicial
print("A temperatura convertida é: {:.2f}".format(temp_final))
while True:
    resposta = input("Deseja realizar outra conversão? (s/n): ")
    if resposta.lower() == 's':
        temp_inicial = float(input("Digite a temperatura que deseja converter (somente números): \n"))
        unidade_entrada = int(input("Escolha a unidade de temperatura de entrada (1. Celsius, 2. Fahrenheit, 3. Kelvin): \n"))
        unidade_saida = int(input("Escolha a unidade de temperatura de saída (1. Celsius, 2. Fahrenheit, 3. Kelvin): \n"))
        if unidade_entrada == 1:  # Celsius
            if unidade_saida == 1:  # Celsius
                temp_final = temp_inicial
            elif unidade_saida == 2:  # Fahrenheit
                temp_final = (temp_inicial * 9/5) + 32
            elif unidade_saida == 3:  # Kelvin
                temp_final = temp_inicial + 273.15
        elif unidade_entrada == 2:  # Fahrenheit
            if unidade_saida == 1:  # Celsius
                temp_final = (temp_inicial - 32) * 5/9
            elif unidade_saida == 2:  # Fahrenheit
                temp_final = temp_inicial
            elif unidade_saida == 3:  # Kelvin
                temp_final = (temp_inicial - 32) * 5/9 + 273.15
        elif unidade_entrada == 3:  # Kelvin
            if unidade_saida == 1:  # Celsius
                temp_final = temp_inicial - 273.15
            elif unidade_saida == 2:  # Fahrenheit
                temp_final = (temp_inicial - 273.15) * 9/5 + 32
            elif unidade_saida == 3:  # Kelvin
                temp_final = temp_inicial
        print("A temperatura convertida é: {:.2f}".format(temp_final))
    elif resposta.lower() == 'n':
        print("Obrigado por usar o programa!")
        break
    else:
        print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")