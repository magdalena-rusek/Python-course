import random as r

data = []

for i in range (0, 50):
 data.append(r.randrange(0,501))

check = data
print(data)	
tmp = 0

for i in range(0, 50):
 for j in range(0, 50):
  if data[i]<data[j]:
   tmp = data[j]
   data[j]=data[i]
   data[i]=tmp

check.sort()
print(data)
print(check)

if data==check:
 print('Poprawne sortowanie')
else:
 print('Niepoprawne sortowanie')
