##Esse programa consistem em descobrir se uma pessoa está apta a tirar a carteira de motorista, para isso é necessário que a pessoa tenha 18 anos ou mais.##
print ("Olá, seja bem-vindo ao programa de verificação de idade para carteira de motorista!")
nome= input ("Digite seu nome:")
ano_nascimento= int(input("Digite o ano do seu nascimento:"))
ano_atual= int(input("Digite o ano atual:"))
idade= ano_atual - ano_nascimento
if idade >= 18:
    print ("Parabéns, {}!\nVocê tem {} anos e está apto(a) a tirar a carteira de motorista.".format(nome, idade))    
else:
    print ("Desculpe, {}!\nVocê tem {} anos e não está apto(a) a tirar a carteira de motorista.".format(nome, idade))