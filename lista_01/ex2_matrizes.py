# 2 multiplique duas matrizes compativeis e verifique a comutatividade
import numpy as np

A = np.array([[1,2,3],
              [4,5,6]])

B = np.array([[1,2],
              [3,4],
              [5,6]])

print("\nMatriz A: \n", A, "\n\nMatriz B: \n", B)

C = np.dot(A,B)
D = np.dot(B,A)

print("\nA multiplicação de AxB: \n", C)
print("\nA multiplicação de BxA: \n", D)

if np.array_equal(C,D):
   print("\nA comutatividade se aplica as duas matrizes. (AxB = BXA)\n")
else:
   print("\nA comutatividade não se aplica as duas matrizes.(AxB != BXA)\n")
