import matplotlib.pyplot as plt
import numpy as np

dados_tabela_aluno_um = [10,5,2,4,6,8]
dados_tabela_aluno_dois = [ 1,2,4,8,7,4]
x = 10*np.array(range(len(dados_tabela_aluno_um)))

plt.plot( x, dados_tabela_aluno_um, 'go') # green bolinha
plt.plot( x, dados_tabela_aluno_um, 'k:', color='orange') # linha pontilha orange

plt.plot( x, dados_tabela_aluno_dois, 'r^') # red triangulo
plt.plot( x, dados_tabela_aluno_dois, 'k--', color='blue')  # linha tracejada azul

plt.axis([-10, 60, 0, 11])
plt.title("Grafico - Lanche")

plt.grid(True)
plt.xlabel("Dias")
plt.ylabel("Consumo")
plt.show()