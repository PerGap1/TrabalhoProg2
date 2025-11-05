def merge_sorter(lista : list):
    if len(lista) > 1:
        metade = len(lista) // 2
        lista_1 = lista[:metade]
        lista_2 = lista[metade:]
        lista.clear()

        merge_sorter(lista_1)
        merge_sorter(lista_2)

        while len(lista_1) > 0 and len(lista_2) > 0:
            if lista_1[0] <= lista_2[0]:
                elem = lista_1.pop(0)
            else:
                elem = lista_2.pop(0)
            lista.append(elem)

        if len(lista_1) == 0:
            lista.extend(lista_2)
        else:
            lista.extend(lista_1)

        # Coloquei essa linha apenas para ter a lista ordenada em mãos quando você chama a função, por pura praticidade.
        # Não é realmente necessária, porque a lista já foi ordenada (e nem está de acordo com a PEP 8 :> )
        return lista