import numpy as np
# funkcja wejsciowa Tm

def sin_Tm(A, f, dt, t_max):  
  # Parametry czasowe
    t = np.arange(0, t_max, dt)

  # Pobudzenie: moment sinusoidalny

    Tm = A * np.sin(2 * np.pi * f * t)

    return t, Tm

def rec_Tm(A,f, dt, t_max):
    # Parametry czasowe
    t = np.arange(0, t_max, dt)

  # Pobudzenie: prostokątny okresowy
    sin_val=np.sin(2 * np.pi * f * t)
    Tm = A * np.where(sin_val >= 0, 1, -1)
    return t, Tm

def trian_Tm(A,f, dt, t_max):
    # Parametry czasowe
    t = np.arange(0, t_max, dt)

    T = 1/f
    t_mod = np.mod(t,T) # czas w jednym okresie
  # Pobudzenie: trójkątny okresowy
    Tm = A * (1 - 4 * np.abs(t_mod / T - 0.5)) # 4 sprawia, że na krańcach (gdy t_mod=0) jest -A, a w środku (dla t_mod=0.5) jest A

    return t, Tm
    
def rec_imp_Tm(A, dt, t_max, T):
    # Parametry czasowe
    t = np.arange(0, t_max, dt)
    t_0=0
    # Pobudzenie: prostokątny impuls
    Tm = A*np.where((t >= t_0) & (t <= t_0+T), 1, 0)

    return t, Tm

def trian_imp_Tm(A, dt, t_max, T):
    # Parametry czasowe
    t = np.arange(0, t_max, dt)
    t_0=0
    t_mod = np.mod(t - t_0, T)
    # Pobudzenie: prostokątny impuls
    signal = A*(1-2*np.abs(t_mod/T-0.5)) # to samo co w okresowym, ale 2, bo na krńcach jest równe 0
    Tm = np.where((t >= t_0) & (t <= t_0+T), signal, 0)

    return t, Tm
