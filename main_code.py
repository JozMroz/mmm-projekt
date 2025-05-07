import numpy as np
import function_gen as fun
import RK4_method as rk
import euler_method as eum
from end_fun import end_fun
from drawing_input import drawing_input
from drawing_output import drawing_output
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

 # Pobranie sygnału wejciowego
while(True):
    signal_type = input("Podaj typ sygnału: ")

    if signal_type == 'sinus':
        ts, Tm_tab = fun.sin_Tm(1, 1, dt, tk)
        break
    elif signal_type == 'triangle':
        ts, Tm_tab = fun.trian_Tm(1, 1, dt, tk)
        break
    elif signal_type == 'rect':
        ts, Tm_tab = fun.rect_Tm(1, 1, dt, tk)
        break
    elif signal_type == 'rect_imp':
        ts, Tm_tab = fun.rec_imp_Tm(1, 1, dt, tk)
        break
    elif signal_type == 'trian_imp':
        ts, Tm_tab = fun.trian_imp_Tm(1, 1, dt, tk)
        break
    else:
        continue
#ts, Tm_tab = fun.sin_Tm(1, 1, dt, tk)
y_eum = np.array([0, 0])      # dla Eulera
y_rk = np.array([0, 0])   # osobna kopia dla RK4
times = []
phis_eum = []
phis_rk = []
omegas_eum = []
omegas_rk = []

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

def result(t, y):
    return end_fun(t, y, dt, Tm_tab, Jeq, beq)

while t<=tk:
    
    times.append(t)
    
    # metoda Eulera
    phis_eum.append(y_eum[0])
    omegas_eum.append(y_eum[1])

    # metoda RK4 
    phis_rk.append(y_rk[0])
    omegas_rk.append(y_rk[1])

    # wykonaj krok dla Eulera i RK4
    y_eum = eum.euler_method(dt, y_eum, t, result)
    y_rk = rk.rk4(result, t, y_rk, dt)
    
    t = t + dt

# Rysowanie sygnału wejsciowego
drawing_input(ts, Tm_tab, signal_type, ylabel=f'Wartosc {signal_type}')

# Rysowanie sygnałów wyjsciowych
drawing_output(times, phis_eum, phis_rk, 'phi')
drawing_output(times, omegas_eum, omegas_rk, 'omega')
