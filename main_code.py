import numpy as np
import matplotlib.pyplot as plt
import function_gen as fun
import RK4_method as rk
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

 # Pobranie czasu symulacji
t=t0=0
tk = float(input("Podaj wartosc tk (czas symulacji) [s]: "))
dt = float(input("Podaj dt (dlugosc kroku) [s]: "))


ts, Tm_tab = fun.sin_Tm(1,1, tk, dt) #przykładowe na razie
y = np.array([0, 0]) #potem z poziomu konsoli bedzie mozna wprowadzic warunki poczatkowe
times = []
phis = []
omegas = []
 # Możliwe zmiany!!!!!!!!!!
""" 
    Możliwe, że zamiast podawania danych z konsoli, zrobimy cos ciekawszego, ale czas pokaze
"""

Jeq = J1 + J2*(n1/n2)**2
beq = b1 + b2*(n1/n2)**2

print("Jeq [kg*m^2]:", Jeq)
print("beq [Nm]:", beq)


# Rownanie stanu
""" 
    Jeq*fi1(t)" = Tm(t) - beq*fi1(t)'
    fi'= w
    w' = fi'' = 1/Jeq*(Tm(t) - w*beq) 
"""
def end_fun(t, y):
    i = int(t / dt)
    if i >= len(Tm_tab):
        Tm = Tm_tab[-1]
    else:
        Tm = Tm_tab[i]
    phi = y[0]
    w = y[1]
    dphi = w
    dw = (Tm - beq * w) / Jeq
    return np.array([dphi, dw])

while t<=tk:
    times.append(t)
    phis.append(y[0])
    omegas.append(y[1])
    y=rk.rk4(end_fun, t, y, dt)
    t=t+dt
