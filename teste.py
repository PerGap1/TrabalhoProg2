import random

def hilarious_merge_sorter(l):
    if len(l) > 1:
        meio = len(l) // 2
        lEsq = l[:meio]
        lDir = l[meio:]

        hilarious_merge_sorter(lEsq) 
        hilarious_merge_sorter(lDir)

        hilarous_merge(l, lEsq, lDir)

def hilarous_merge(l, lEsq, lDir):
    i = 0
    j = 0
    k = 0

    while i < len(lEsq) and j < len(lDir):
        if lEsq[i] < lDir[j]:
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


lista = []
for i in range(100):
    lista.append( random.randint(1, 1000) )

print(lista)

print()

hilarious_merge_sorter(lista)

print(lista)