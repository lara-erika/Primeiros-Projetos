#este esxercicio consiste em informar se um aluno foi aprovado ou não##
nome= input("Digite o nome do aluno:")
nota1= float(input("Digite a primeira nota:"))
nota2= float(input("Digite a segunda nota:"))
media= (nota1+nota2)/2
pontoextra= float(input("Digite a nota do ponto extra:"))
mediafinal= (media+pontoextra)
if mediafinal >= 6:
    print("Parabéns, {}! Você foi aprovado com média final de {}".format(nome, mediafinal)) 
else:
    print("Desculpe, {}! Você foi reprovado com média final de {}".format(nome, mediafinal))
