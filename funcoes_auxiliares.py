import leitor_arquivo

def total_pontos(matricula):
    pontos = leitor_arquivo.retorna_pontos()
    alunos = leitor_arquivo.retorna_alunos()

    # Garante que o aluno está no dicionário
    if matricula not in alunos:
        return -1
    
    lista_atividades = alunos[matricula][1]

    soma_pontos = 0

    # Itera pelas atividades realizadas pelo aluno
    for tipo_ativ, codigo_ativ, unidades in lista_atividades:
        _, pontos_unidade, _ = pontos[ (tipo_ativ, codigo_ativ) ]
        soma_pontos += pontos_unidade * unidades

    # Máximo 15 pontos
    return soma_pontos if soma_pontos < 15 else 15