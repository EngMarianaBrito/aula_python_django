print("\tSeja Bem vindo")
print("="*30)
funcionario_icev ={
    'Euzebio': 96556,
    'Bruna'  : 10959,
    'Arthur' : 46161  
}

funcionario_novo = input("Digite o nome do funcionario: ")
codigo = float(input("Numero do Codigo de acesso: "))

if funcionario_icev.get(funcionario_novo):
    print("Ja existe um funcionario com esse usuario ",funcionario_novo)
else:
    funcionario_icev[funcionario_novo] = codigo
print(funcionario_icev)
