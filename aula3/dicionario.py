dicionario_vazio = {}
print(dicionario_vazio)

#dicionario_1 = {"nome","Lia Mariana","Idade","20"}
dicionario_1 = {
    "nome":"Lia",
    "idade":"20"
}
print(dicionario_1)

dicionario_1["nome"] = "Mariana"
print(dicionario_1)

dicionario_1["altura"] = "1.60"
print(dicionario_1)

del(dicionario_1["altura"])
print(dicionario_1)