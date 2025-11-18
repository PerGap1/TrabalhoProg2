def compara():
    with open("saida.txt", "r") as arquivo:
        nossa_saida = arquivo.readlines()

    with open("modelos_saida\saida4.txt", "r") as arquivo:
        saida1 = arquivo.readlines()

    cont = 0
    for linha1, linha2 in zip(nossa_saida, saida1):
        if linha1 != linha2:
            print(linha1)
            cont += 1
        
    print(cont)

compara()