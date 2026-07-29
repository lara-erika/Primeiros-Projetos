## Exercicio do curso de Python do IFES; Entradas: votos, horario; processamento: ler voto, verificar horario se esta entre 8h e 17h; saída: total de votos por candidato ##
horario = 8
candidato1=0
candidato2=0
nulo=0
while (horario<17):
    voto = int(input("Voto:"))
    if (voto==22):
        print("Voto para candidato 1")
        candidato1=candidato1+1
    elif (voto==13):
        print("Voto para candidato 2")
        candidato2=candidato2+1
    else:
        print("Voto nulo")
        nulo=nulo+1
    horario = int(input("Horário:"))