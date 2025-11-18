import funcoes_auxiliares
import leitor_arquivo
import random

def quick_sorter(lista: list, inf=0, sup=None, alunos:list=None, pontos:list=None, random_pivot=False):
    
    if alunos is None or pontos is None:
        alunos = leitor_arquivo.retorna_alunos()
        pontos = leitor_arquivo.retorna_pontos()

    if sup is None: 
        sup = len(lista)-1

    if inf < sup:
        pos = qs_particao(lista, inf, sup, alunos, pontos, random_pivot)
        quick_sorter(lista, inf, pos-1, alunos, pontos)
        quick_sorter(lista, pos+1, sup, alunos, pontos)

def qs_particao(l, inf, sup, alunos:list, pontos:list, random_pivot):
    # --- NEW: choose pivot randomly ---
    if random_pivot:
        p = random.randint(inf, sup)
        l[inf], l[p] = l[p], l[inf]
    # ----------------------------------

    pivot = l[inf]
    i = inf + 1
    j = sup

    while i <= j:
        while i <= j and (l[i] == pivot or menor_que(l[i], pivot, alunos, pontos)):
            i += 1
        while j >= i and (l[j] != pivot and not menor_que(l[j], pivot, alunos, pontos)):
            j -= 1
        if i < j: 
            l[i], l[j] = l[j] , l[i]

    l[inf], l[j] = l[j], l[inf]
    return j

def merge_sorter(lista: list, alunos:list=None, pontos:list=None):
    if alunos is None or pontos is None:
        alunos = leitor_arquivo.retorna_alunos()
        pontos = leitor_arquivo.retorna_pontos()

    if len(lista) > 1:
        metade = len(lista) // 2
        lista_1 = lista[:metade]
        lista_2 = lista[metade:]
        lista.clear()

        merge_sorter(lista_1, alunos, pontos)
        merge_sorter(lista_2, alunos, pontos)

        merge(lista, lista_1, lista_2, alunos, pontos)


def merge(lista, lista_1, lista_2, alunos, pontos):
    while len(lista_1) > 0 and len(lista_2) > 0:
        if menor_que(lista_1[0], lista_2[0], alunos, pontos):
            elem = lista_1.pop(0)
        else:
            elem = lista_2.pop(0)
        lista.append(elem)

    if len(lista_1) == 0:
        lista.extend(lista_2)
    else:
        lista.extend(lista_1)


def menor_que(aluno_1, aluno_2, alunos:list, pontos:list):
    matricula_1 = aluno_1[0]
    matricula_2 = aluno_2[0]

    # Tenta verificar pelo 1º critério: pontos
    pontos_1 = funcoes_auxiliares.total_pontos(matricula_1, alunos, pontos)
    pontos_2 = funcoes_auxiliares.total_pontos(matricula_2, alunos, pontos)
    if pontos_1 != pontos_2: return pontos_1 > pontos_2

    # Tenta verificar pelo 2º critério: nome
    nome_1 = alunos[matricula_1][0]
    nome_2 = alunos[matricula_2][0]
    if nome_1 != nome_2: return nome_1 < nome_2

    # Tenta verificar pelo 3º critério: matrícula
    if matricula_1 != matricula_2: return matricula_1 < matricula_2

    # Tenta verificar pelo 4º critério: tipo da atividade
    index_ativ_1 = aluno_1[1]           # Esses dois valores vêm da lista a ser ordenada
    index_ativ_2 = aluno_2[1]

    tupla_ativ_1 = alunos[matricula_1][1][index_ativ_1]
    tupla_ativ_2 = alunos[matricula_2][1][index_ativ_2]

    tipo_ativ_1 = tupla_ativ_1[0]
    tipo_ativ_2 = tupla_ativ_2[0]

    if tipo_ativ_1 != tipo_ativ_2: return tipo_ativ_1 < tipo_ativ_2

    # Tenta verificar pelo último critério: código da atividade
    codigo_ativ_1 = tupla_ativ_1[1]
    codigo_ativ_2 = tupla_ativ_2[1]
    return codigo_ativ_1 < codigo_ativ_2


def verifica_se_ordenada(lista):
    alunos = leitor_arquivo.retorna_alunos()
    pontos = leitor_arquivo.retorna_pontos()

    for index in range(len(lista) - 1):
        elem_1 = lista[index]
        elem_2 = lista[index + 1]

        if not menor_que(elem_1, elem_2, alunos, pontos) and elem_1 != elem_2:
            return False
    
    return True