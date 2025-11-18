import pickle

caminho_arquivo = r"entrada3.bin"

def retorna_tipos():
    with open(caminho_arquivo, "rb") as arquivo:
        return pickle.load(arquivo)
    

def retorna_pontos():
    with open(caminho_arquivo, "rb") as arquivo:
        _ = pickle.load(arquivo)
        return pickle.load(arquivo)
    

def retorna_alunos():
    with open(caminho_arquivo, "rb") as arquivo:
        _ = pickle.load(arquivo)
        _ = pickle.load(arquivo)
        return pickle.load(arquivo)


def retorna_lista_principal():
    dici_alunos = retorna_alunos()
    lista_retorno = []

    for matricula in dici_alunos:
        _, lista_atividades = dici_alunos[matricula]

        # Não sei o porquê de um padrão tão ruim
        for i in range(len(lista_atividades)):
            lista_retorno.append( (matricula, i) )

    return lista_retorno