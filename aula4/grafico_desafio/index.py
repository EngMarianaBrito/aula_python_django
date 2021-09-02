import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def grafico_pizza():  
    dados = [] 
    labels = ["dados1","dados2","dados3","dados4","dados5"]

    plt.title("Gráfico Pizza")

    #dados
    while len(dados) < 5:
        dados_d = input("Escreva um numero: ")
        if dados_d in dados:
            print("Digite outro numero: ")
        else:
            dados.append(dados_d)
 
    plt.pie(dados,labels=labels)
    plt.legend(labels, loc=3)
    plt.savefig('grafico_pizza.png', transparent = True)#salvar grafico
    plt.show()

def grafico_gantt():
    plt.title("Gráfico Gant")
    
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

def grafico_3d():
    plt.title("Gráfico 3D")
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    dado_1, dado_2 ,dado_3 = axes3d.get_test_data(0.10)#implementando dados
    
    ax.plot_wireframe( dado_1, dado_2 ,dado_3,rstride = 30, cstride = 30)
    
    plt.style.use('ggplot')#mudar estilo
    plt.savefig('grafico_3d.png', transparent = True)#salvar grafico
    plt.show()

def grafico_linha():
    #grafico linha
    plt.title("Consumo de café por mes")

    
    plt.plot(x=[1,2,3,4,5,6],y=[3,2,4,7,9,10])
    plt.ylabel("Meses")
    plt.xlabel("Consumo")

    plt.savefig('grafico_Linha.png', transparent = True)#salvar grafico
    plt.show()

def grafico_barra():
    plt.title("Medias de meninas e meninos")

    sexo = ["Meninos","Meninas"]
    porcentagem = [45,55]

    plt.bar(sexo,porcentagem)
    plt.savefig('grafico_barra.png', transparent = True)#salvar grafico
    plt.show()