import numpy as np
import matplotlib.pyplot as plt

# Przekładnia model

#Zmienne
"""
Zmienne:
Tm       - moment dostarczony do układu [Nm]
b1, b2   - współczynniki tłumienia [Nm*s/rad]
J1, J2   - momenty bezwładności wałów [kg*m^2]
fi1, fi2 - położenia kątowe wałów [rad]
n1, n2   - przełożenia przekładni 
"""
 # Pobranie wartosci wspolczynnikow tlumienia
b1 = float(input("Podaj wartosc b1 [Nm]: "))
b2 = float(input("Podaj wartosc b2 [Nm]: "))

 # Pobranie wartosci przelozen przekładni
n1 = float(input("Podaj wartosc n1: "))
n2 = float(input("Podaj wartosc n2: "))

 # Pobranie wartosci momentów bezwładnosci walow
J1 = float(input("Podaj wartosc J1 [kg*m^2]: "))
J2 = float(input("Podaj wartosc J2 [kg*m^2]: "))

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

print("Jeq [kg*m^2]:", Jeq)
print("beq [Nm]:", beq)