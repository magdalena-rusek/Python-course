import os

def wypisz(katalog):
 for element in os.listdir(katalog):
  sciezka = os.path.join(katalog, element)
  print(sciezka)
  if os.path.isdir(sciezka):
   wypisz(sciezka)

wypisz("/dev")

