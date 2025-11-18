import leitor_arquivo, sorting, funcoes_auxiliares
from time import time

def teste():
    '''
    Aqui dá pra fazer um teste inicial do sistema
    Pra mudar o tamanho do arquivo usado, vai em leitor_arquivo,
    e muda o número do caminho pro txt.
    1: 10 elementos
    2: 100 elementos
    3: 1000 elementos
    4: 10000 elementos
    '''
    lista = leitor_arquivo.retorna_lista_principal()

    print("Ordenada") if sorting.verifica_se_ordenada(lista) else print("Não ordenada")

    t1 = time()
    sorting.merge_sorter(lista)
    t2 = time()

    print("Ordenada") if sorting.verifica_se_ordenada(lista) else print("Não ordenada")
    print(f"Tempo: {(t2 - t1):.3f} segundos")


def main():
    lista = leitor_arquivo.retorna_lista_principal()
    sorting.merge_sorter(lista)

    # with open(r"saida.txt", "w") as arquivo:
        # funcoes_auxiliares.saida(lista, arquivo)

if __name__ == "__main__":
    t1 = time()
    main()
    t2 = time()

    print(f"{(t2 - t1):.2f}")