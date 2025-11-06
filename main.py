import leitor_arquivo, sorting
from time import time

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