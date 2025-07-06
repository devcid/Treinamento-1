import numpy as np 


equacoes = [[3,1,-1],
            [2,-2,4],
            [-1,0.5,-1]]

independentes = [1,-2,0]

condicao = np.linalg.cond(equacoes)

print(condicao)