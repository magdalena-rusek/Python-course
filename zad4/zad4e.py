import numpy as n
from numpy import random

row = 8
col = 8

matrix1 = random.randint(10, size=(row,col))
matrix2 = random.randint(10, size=(row,col))

iloczyn = n.zeros([row, col])

for i in range(0, row):
 for j in range(0, col):
  for k in range(0, col):
   iloczyn[i][j] += matrix1[i][k] * matrix2[k][j]
 
print('Macierz1: \n', matrix1)
print('\nMacierz2: \n', matrix2)
print('\nIloczyn tych macierzy: \n', iloczyn)


