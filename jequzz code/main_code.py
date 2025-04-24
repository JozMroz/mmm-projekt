import numpy as np
import matplotlib.pyplot as plt

# Przekładnia model

#Zmienne
"""
Zmienne:
Tm       - moment dostarczony do układu
b1, b2   - współczynniki tłumienia
J1, J2   - momenty bezwładności wałów
fi1, fi2 - położenia kątowe wałów
n1, n2   - przełożenia przekładni
"""
 # Pobranie wartosci wspolczynnikow tlumienia
b1 = float(input("Podaj wartosc b1: "))
b2 = float(input("Podaj wartosc b2: "))

 # Pobranie wartosci przelozen przekładni
n1 = float(input("Podaj wartosc n1: "))
n2 = float(input("Podaj wartosc n2: "))

 # Pobranie wartosci momentów bezwładnosci walow
J1 = float(input("Podaj wartosc J1: "))
J2 = float(input("Podaj wartosc J2: "))

 # Możliwe zmiany!!!!!!!!!!
""" 
    Możliwe, że zamiast podawania danych z konsoli, zrobimy cos ciekawszego, ale czas pokaze
"""

 # Rownanie stanu
""" 
    Jeq*fi1(t)" = Tm - beq*fi1(t)'
"""
Jeq = J1 + J2*(n1/n2)**2
beq = b1 + b2*(n1/n2)**2

print("Jeq:", Jeq)
print("beq:", beq)