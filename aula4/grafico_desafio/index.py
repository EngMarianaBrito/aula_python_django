import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

def grafico_1():  
    dados= []
    while len(dados) < 5:
        dados_d = input("Escreva um numero: ")
        if dados_d in dados:
            print("Nao pode escrever esse numero.")
        else:
            dados.append(dados_d)

    plt.pie(dados)
    plt.savefig('grafico_gantt.png', transparent = True)#salvar grafico
    plt.show()

def grafico_2():
    fig, gantt = plt.subplots() 
    gantt.set_ylim(0, 50) 

    gantt.set_yticks([15, 25, 35]) 
    gantt.set_yticklabels(['1', '2', '3']) 
    
    gantt.grid(True) 
    
    gantt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:red')) 
    gantt.broken_barh([(110, 10), (150, 10)], (10, 9), 
                            facecolors ='tab:blue') 
    
    gantt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), 
                                    facecolors =('tab:green')) 
    
    
    plt.style.use('ggplot')#mudar estilo
    plt.savefig('grafico_gantt.png', transparent = True)#salvar grafico
    plt . show ()

def grafico_3():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    dado_1, dado_2 ,dado_3 = axes3d.get_test_data(0.10)#implementando dados
    
    ax.plot_wireframe( dado_1, dado_2 ,dado_3,rstride=20, cstride=20)
    
    plt.style.use('ggplot')#mudar estilo
    plt.savefig('grafico_gantt.png', transparent = True)#salvar grafico
    plt.show()