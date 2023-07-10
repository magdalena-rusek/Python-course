import numpy as n
from numpy import random

row = 128
col = 128

matrix1 = random.randint(10, size=(row,col))
matrix2 = random.randint(10, size=(row,col))

suma = n.zeros([row, col])

for i in range(0, row):
 for j in range(0, col):
  suma[i][j] = matrix1[i][j] + matrix2[i][j]
 
print('Macierz1: \n', matrix1)
print('\nMacierz2: \n', matrix2)
print('\nSuma tych macierzy: \n', suma)


