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

x = Zespolona(4, 3)
y = Zespolona(12, -2)

print('Liczba1: ')
x.printuj()
print('\nLiczba2: ')
y.printuj()

suma = dodaj(x, y)
roznica = odejmij(x, y)
iloczyn = pomnoz(x, y)
iloraz = podziel(x, y)
x.sprzezenie()

print('\nSuma: ')
suma.printuj()
print('\nRóżnica: ')
roznica.printuj()
print('\nIloczyn: ')
iloczyn.printuj()
print('\nIloraz: ')
iloraz.printuj()
print('\nSprzężenie liczby1: ')
x.printuj()
