import tkinter as tk
from tkinter import ttk
import numpy as np
import function_gen as fun
import RK4_method as rk
import euler_method as eum
from end_fun import end_fun
from drawing_input import drawing_input
from drawing_output import drawing_output
import matplotlib.pyplot as plt

# Przekładnia model
def simulation():

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
    b1 = float(entry_b1.get())
    b2 = float(entry_b2.get())

    # Pobranie wartosci przelozen przekładni
    n1 = float(entry_n1.get())
    n2 = float(entry_n2.get())

    # Pobranie wartosci momentów bezwładnosci walow
    J1 = float(entry_J1.get())
    J2 = float(entry_J2.get())

    # Pobranie czasu symulacji
    t=t0=0
    tk = float(entry_tk.get())
    dt = float(entry_dt.get())

    # Pobranie sygnału wejciowego
    while(True):
       signal_type = signal_var.get()

       if signal_type == 'sinus':
           A = float(entry_A.get())
           f = float(entry_f.get())
           ts, Tm_tab = fun.sin_Tm(A, f, dt, tk)
           break
       elif signal_type == 'triangle':
           A = float(entry_A.get())
           f = float(entry_f.get())
           ts, Tm_tab = fun.trian_Tm(A, f, dt, tk)
           break
       elif signal_type == 'rect':
           A = float(entry_A.get())
           f = float(entry_f.get())
           ts, Tm_tab = fun.rec_Tm(A, f, dt, tk)
           break
       elif signal_type == 'rect_imp':
           A = float(entry_A.get())
           T = float(entry_T.get())
           ts, Tm_tab = fun.rec_imp_Tm(A, dt, tk, T)
           break
       elif signal_type == 'trian_imp':
           A = float(entry_A.get())
           T = float(entry_T.get())
           ts, Tm_tab = fun.trian_imp_Tm(A, dt, tk, T)
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
    plt.show()

# Interfejs Tkinter
root = tk.Tk()
root.title("Symulator przekładni")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

label_b1 = ttk.Label(frame, text="b1 [Nm]:")
label_b1.grid(column=0, row=0)
entry_b1 = ttk.Entry(frame)
entry_b1.grid(column=1, row=0)

label_b2 = ttk.Label(frame, text="b2 [Nm]:")
label_b2.grid(column=0, row=1)
entry_b2 = ttk.Entry(frame)
entry_b2.grid(column=1, row=1)

label_n1 = ttk.Label(frame, text="n1:")
label_n1.grid(column=0, row=2)
entry_n1 = ttk.Entry(frame)
entry_n1.grid(column=1, row=2)

label_n2 = ttk.Label(frame, text="n2:")
label_n2.grid(column=0, row=3)
entry_n2 = ttk.Entry(frame)
entry_n2.grid(column=1, row=3)

label_J1 = ttk.Label(frame, text="J1 [kg*m^2]:")
label_J1.grid(column=0, row=4)
entry_J1 = ttk.Entry(frame)
entry_J1.grid(column=1, row=4)

label_J2 = ttk.Label(frame, text="J2 [kg*m^2]:")
label_J2.grid(column=0, row=5)
entry_J2 = ttk.Entry(frame)
entry_J2.grid(column=1, row=5)

label_tk = ttk.Label(frame, text="Czas symulacji [s]:")
label_tk.grid(column=0, row=6)
entry_tk = ttk.Entry(frame)
entry_tk.grid(column=1, row=6)

label_dt = ttk.Label(frame, text="Krok symulacji [s]:")
label_dt.grid(column=0, row=7)
entry_dt = ttk.Entry(frame)
entry_dt.grid(column=1, row=7)

signal_var = tk.StringVar(value="sinus")
signal_menu = ttk.OptionMenu(frame, signal_var, "sinus", "triangle", "rect", "rect_imp", "trian_imp")
signal_menu.grid(column=1, row=8)

label_A = ttk.Label(frame, text="Amplituda:")
label_A.grid(column=0, row=9)
entry_A = ttk.Entry(frame)
entry_A.grid(column=1, row=9)

label_f = ttk.Label(frame, text="Częstotliwość [Hz]:")
label_f.grid(column=0, row=10)
entry_f = ttk.Entry(frame)
entry_f.grid(column=1, row=10)


label_T = ttk.Label(frame, text="Długość impulsu:")
entry_T = ttk.Entry(frame)

signal_var.trace_add("write", lambda *args: (
    [label_T.grid(column=0, row=11), entry_T.grid(column=1, row=11)]
    if signal_var.get() in ['rect_imp', 'trian_imp'] 
    else [label_T.grid_remove(), entry_T.grid_remove()]
))

run_button = ttk.Button(frame, text="Start", command=simulation)
run_button.grid(column=1, row=12)

root.mainloop()
