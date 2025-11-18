import matplotlib.pyplot as plt

# Deixei as funções que eu fiz em outro programa caso você queria visualizar os sorters funcionando
# A primeira é chamada pra iniciar o gráfico, e ela retorna bars, que deve ser armazenado e usado depois
# A segunda recebe as bars (colunas do gráfico), e atualiza o gráfico já montado com os novos dados passados


def iniciar_grafico(lista, tipo):
    input("Confirmar")
    plt.clf()
    plt.ion()  # modo interativo
    bars = plt.bar(range(len(lista)), lista, color='skyblue')
    plt.title(tipo)
    return bars


def atualizar_grafico(bars, lista, passo):
    for bar, val in zip(bars, lista):
        bar.set_height(val)
    plt.title(f"Passo {passo}")
    plt.pause(0.00001)

iniciar_grafico