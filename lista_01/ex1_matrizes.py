import numpy as np 

# 1 crie uma matriz 3x3 com valores aleatorios, calcule sua transposta, determinante e inversa

mat1 = np.random.randint(11 ,size = (3,3)) #cria matriz de inteiros para melhor vizualização

print("\nEsta é a matriz gerada: \n", mat1)

tsp_mat1 = mat1.transpose()

print("\nEsta é a matriz trasnposta:\n", tsp_mat1) # pela documentação também é possivel fazer somente com mat1.T elimina a linha 9

det_mat1 = np.linalg.det(mat1)

print("\nO determinante da matriz é:", det_mat1)

inv_mat1 = np.linalg.inv(mat1)

print("\nA inversa da matriz é: \n", inv_mat1)