class Zespolona:
 def __init__(self, real, imag): 
  self.real = real
  self.imag = imag
 def sprzezenie(self):
  self.imag = -self.imag

 def printuj(self):
  print(self.real, '+ j*', self.imag)

def dodaj(c1, c2):
 suma = Zespolona(c1.real+c2.real, c1.imag+c2.imag) 
 return suma

def odejmij(c1, c2):
 roznica = Zespolona(c1.real-c2.real, c1.imag-c2.imag) 
 return roznica

def pomnoz(c1, c2):
 r = c1.real*c2.real-c1.imag*c2.imag
 i = c1.real*c2.imag+c1.imag*c2.real
 iloczyn = Zespolona(r, i) 
 return iloczyn

def podziel(c1, c2):
 r = (c1.real*c2.real+c1.imag*c2.imag)/((c2.real**2)+(c2.imag**2))
 i = (c1.imag*c2.real-c1.real*c2.imag)/((c2.real**2)+(c2.imag**2))
 iloraz = Zespolona(r, i) 
 return iloraz

print('Postac równania: (a+jb) [znak] (c+jd)')
a = int(input('a = '))
b = int(input('b = '))
znak = input('znak: ' )
c = int(input('c = ' ))
d = int(input('d = ' ))

x = Zespolona(a, b)
y = Zespolona(c, d)

if znak=='+':
 wyn = dodaj(x, y)
 print('Wynik: ')
 wyn.printuj()
elif znak=='-':
 wyn = odejmij(x, y)
 print('Wynik: ')
 wyn.printuj()
elif znak=='*':
 wyn = pomnoz(x, y)
 print('Wynik: ')
 wyn.printuj()
elif znak=='/':
 wyn = podziel(x, y)
 print('Wynik: ')
 wyn.printuj()
else:
 print('Wprowadzone dane są niepoprawne!')


