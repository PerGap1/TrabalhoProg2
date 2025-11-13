import leitor_arquivo

def total_pontos(matricula, alunos=[], pontos=[]):
    if len(alunos) == 0 or len(pontos) == 0:
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


def saida(lista, arquivo=None):
    dicionario_alunos = leitor_arquivo.retorna_alunos()
    dicionario_pontos = leitor_arquivo.retorna_pontos()
    matricula_anterior = 0

    for matricula, index_atividade in lista:
        nome, lista_atividades = dicionario_alunos[matricula]
        tipo_ativ, codigo_ativ, unidades = lista_atividades[index_atividade]
        nome_ativ, pontos_por_ativ, _ = dicionario_pontos[(tipo_ativ, codigo_ativ)]

        soma_pontos = total_pontos(matricula)

        if matricula != matricula_anterior:
           arquivo.write(f"{nome} ({matricula}): {soma_pontos} pontos\n")

        arquivo.write(f"\t{tipo_ativ}.{codigo_ativ} {nome_ativ}: {unidades}x{pontos_por_ativ}={unidades * pontos_por_ativ}")

        if (matricula, index_atividade) != lista[-1]:
            arquivo.write("\n")

        matricula_anterior = matricula