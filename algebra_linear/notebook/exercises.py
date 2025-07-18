# %%
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
# %%
# Suponhamos que a seguinte matriz forneça as quantidades das vitaminas A, B e C obtidas em cada unidade dos alimentos I e II.
matriz_vitaminas = np.array([
    [4, 3, 0],
    [5, 0, 1]
])
print(matriz_vitaminas)
print(matriz_vitaminas.shape)

# Se ingerirmos 5 unidades do Alimento I e 2 unidades do Alimento II, quanto consumiremos de cada tipo de vitamina?

quantidades_consumidas = np.array([
    [5, 2]
])
total_vitaminas = quantidades_consumidas @ matriz_vitaminas  
total_vitaminas
# %%
# Se o custo dos alimentos depender somente do seu conteúdo vitamínico e soubermos que os preços por unidade de vitamina A, B e C
# são, respectivamente, 1.5, 3 e 5 u.c.p., quanto pagaríamos pela porção de alimentos indicada anteriormente?
precos = np.array([
    [1.5, 3, 5]
])
pagamento_p_porcao = (total_vitaminas * precos).sum()
pagamento_p_porcao

# Ou seja, pagaríamos 100 u.c.p.

# %%
A = np.array([
    [1, 2, 3],
    [2, 1, -1]
])

B = np.array([
    [-2, 0, 1],
    [3, 0, -1]
])

C = np.array([
    [-1, 2, 4]
])

D = np.array([
    [2, -1]
])

# Encontre:
# a) A + B
# b) A * C
# c) B * C
# d) C * D
# e) D * A
# f) D * B
# g) -A
# h) -D

# %%
print(A + B)
# %%
print(A * C)
# %%
print(B * C)
# %%
#print(C * D)
# %%
#print(D * A)
# %%
#print(D * B)

