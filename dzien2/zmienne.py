imie = "Joanna"
nazwisko = "Kowalska"
wiek = 34

print(imie+' '+nazwisko+' '+ 'ma' + " " + str(wiek) + 'lata.') # pamietac aby zamienic wiek na string

print(f"{imie} {nazwisko} ma {wiek} lata.") # formatowanie stringów za pomoca f (space pomiedzy słowami)

print("{0} {1} ma {2} lata.").format(imie,nazwisko,wiek) # to samo co u góry ale w starszek wersji