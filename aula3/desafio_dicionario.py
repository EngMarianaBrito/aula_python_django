engenharia={'João'   :  9,
       'Maria'  : 10,
       'José'   : 4  }

nome = input("Digite o nome do aluno: ")
nota = float(input("Nota dele: "))

if engenharia.get(nome):
    print("Ja existe o aluno ",nome)
else:
    engenharia[nome] = nota
print(engenharia)
