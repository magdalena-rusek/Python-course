import numpy as n
from numpy import random

row = 3
col = 3

m = random.randint(10, size=(row,col))

p = m[0][0]*m[1][1]*m[2][2]+m[0][1]*m[1][2]*m[2][0]+m[0][2]*m[1][0]*m[2][1]
n = m[2][0]*m[1][1]*m[0][2]+m[2][1]*m[1][2]*m[0][0]+m[2][2]*m[1][0]*m[0][1]

det = p-n
print('Macierz: \n', m)
print('\nWyznacznik: ', det)

