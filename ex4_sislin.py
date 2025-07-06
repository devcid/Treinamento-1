import numpy as np

equacoes = [ [3,1,-1],
        [2,-2,4],
        [-1,0.5,-1]]

independentes = [1,-2,0]

resultados = np.linalg.solve(equacoes,independentes)

print("\nvalores de \nx=", resultados[0], "\ny=", resultados[1], "\nz=",resultados[2])