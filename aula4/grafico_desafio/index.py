import matplotlib.pyplot as plt
import numpy as np


def grafico_1():

    dados_tabela_aluno_um = [1,3,5,7,9]
    dados_tabela_aluno_dois = [2,4,6,8,10]
   
    x = 10*np.array(range(len(dados_tabela_aluno_um)))

    plt.plot( x, dados_tabela_aluno_um, 'go') # green bolinha
    plt.plot( x, dados_tabela_aluno_um, 'k:', color='blue') # linha pontilha orange

    plt.plot( x, dados_tabela_aluno_dois, 'r^') # red triangulo
    plt.plot( x, dados_tabela_aluno_dois, 'k--', color='red')  # linha tracejada azul

    plt.axis([-10, 60, 0, 11])
    plt.title("Grafico - Lanche")

    plt.grid(True)
    plt.xlabel("Dias")
    plt.ylabel("Consumo")
    plt.show()

def grafico_2():
    produtos = []
    produtos.append