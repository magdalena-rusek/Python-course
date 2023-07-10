a = float(input('Podaj współczynnik a: '))
b = float(input('Podaj współczynnik b: '))
c = float(input('Podaj współczynnik c: '))

print('Równanie ma postać: y = ', a, 'x*x + ', b, 'x + ', c)
delta = b**2 - 4*a*c
pierwDelta = delta**(1/2)

if delta>0:
 x1 = (-b-pierwDelta)/(2*a)
 x2 = (-b+pierwDelta)/(2*a)
 print('To równanie ma 2 pierwiastki: x1 =', x1, ' oraz x2 =', x2)
elif delta==0:
 x = -b/(2*a)
 print('To równanie ma 1 pierwiastek: x =', x)
else:
 print('To równanie nie ma pierwiastków!')
