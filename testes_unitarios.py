from sorting import merge_sorter
from random import randint
from time import time

def gera_lista():
    tamanho = int(input("Tamanho da lista: "))
    return [randint(0, 10) for _ in range(tamanho)]

def ordenada(lista):
    for index in range(len(lista) - 1):
        if lista[index] > lista[index + 1]:
            return "não ordenada"
    return "ordenada"

def imprime_lista(lista):
    if len(lista) < 11:
        for elem in lista:
            print(elem, end=" ")
        print()

def testa_merge_sorter():
    lista = gera_lista()
    imprime_lista(lista)

    t1 = time()
    imprime_lista(merge_sorter(lista))
    t2 = time()

    print(f"{(t2 - t1):.3f} segundos")
    print(ordenada(lista))

testa_merge_sorter()