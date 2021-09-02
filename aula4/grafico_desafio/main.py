from index import *

print("=" * 25)
print("\tBem Vindo")
print("=" * 25)
print("Escolha o grafico desejado abaixo")

opcao = True

while opcao : 
    print("""
    1.Grafico Pizza
    2.Grafico Gantt
    3.Grafico 3D
    4.Grafico Linha
    5.Grafico de Barra 
    6.Sair
    """)

    opcao = input("Qual opção deseja? Digite um numero: ")
    
    if opcao == "1":
        grafico_pizza()
    elif opcao == "2":
        grafico_gantt()
    elif opcao == "3":
        grafico_3d()
    elif opcao == "4":
        grafico_linha()
    elif opcao == "5":
        grafico_barra()
    elif opcao == "6":
        print("Até mais")
        opcao = None

    else:
        print("Opção Invalida")


