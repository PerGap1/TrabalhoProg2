import funcoes_auxiliares
import leitor_arquivo
import random

def merge_sorter(l, alunos:list=None, pontos:list=None):
    if alunos is None or pontos is None:
        alunos = leitor_arquivo.retorna_alunos()
        pontos = leitor_arquivo.retorna_pontos()

    if len(l) > 1:
        meio = len(l) // 2
        lEsq = l[:meio]
        lDir = l[meio:]

        merge_sorter(lEsq, alunos, pontos) 
        merge_sorter(lDir, alunos, pontos)

        merge(l, lEsq, lDir, alunos, pontos)

def merge(l, lEsq, lDir, alunos:list, pontos:list):
    i = 0
    j = 0
    k = 0

    while i < len(lEsq) and j < len(lDir):
        if menor_que(lEsq[i], lDir[j], alunos, pontos):
            l[k] = lEsq[i]
            i += 1
        else:
            l[k] = lDir[j]
            j += 1
        k += 1
    
    while i < len(lEsq):
        l[k] = lEsq[i]
        i += 1
        k += 1

    while j < len(lDir):
        l[k] = lDir[j]
        j += 1
        k += 1

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