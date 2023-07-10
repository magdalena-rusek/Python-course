try:
 kod = int(input("Ustaw kod (może składać się z samych cyfr): "))
 print("Zapisano kod!")

 nowyKod = int(input('Podaj poprawny kod: '))

 if kod == nowyKod:
  print('Hurra! Podałeś poprawny kod!')
 else:
  print('Wprowadzony kod jest niepoprawny!')

except:
 print("Błąd!")

