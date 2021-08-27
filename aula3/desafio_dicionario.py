#"Pefume"
print("="*30)
print("\tSeja Bem vindo")
print("="*30)

#cadastrando funcionario inicias
funcionario_icev ={
    'Euzebio': 96556, 
    'Bruna'  : 10959,
    'Arthur' : 46161  
}

#cadastrando funcionarios novos 
funcionario_novo = input("Digite o nome do funcionario: ")
codigo = float(input("Numero do Codigo de acesso: "))

#verificando funcionarios adicionados 
if funcionario_icev.get(funcionario_novo):
    print("Ja existe um funcionario com esse usuario ",funcionario_novo)
else:
    funcionario_icev[funcionario_novo] = codigo
    
#imprimindo funcionarios 
print(funcionario_icev)
