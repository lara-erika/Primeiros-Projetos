#Este programa consiste em calcular a área de uma parede e a quantidade de tinta necessária para pintá-la, considerando que 1 litro de tinta pinta 2 metros quadrados.#
print("Bem-vindo ao programa de cálculo de tinta!")
largura = float(input("Digite a largura da parede em metros:\n")) 
altura = float(input("Digite a altura da parede em metros:\n"))
area = largura * altura
quantidade_tinta = area / 2
print("A área da parede é: {:.2f} m²".format(area))
print("A quantidade de tinta necessária é: {:.2f} litros".format(quantidade_tinta))
while True:
    resposta = input("Deseja calcular para outra parede? (s/n): ")
    if resposta.lower() == 's':
        largura = float(input("Digite a largura da parede em metros:\n")) 
        altura = float(input("Digite a altura da parede em metros:\n"))
        area = largura * altura
        quantidade_tinta = area / 2
        print("A área da parede é: {:.2f} m²".format(area))
        print("A quantidade de tinta necessária é: {:.2f} litros".format(quantidade_tinta))
    elif resposta.lower() == 'n':
        print("Obrigado por usar o programa!")
        break
    else:
        print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")