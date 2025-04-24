# funkcja wejsciowa Tm

def sin_Tm(A, f):  
  # Parametry czasowe
    t_max = 5         # czas symulacji (sekundy)
    dt = 0.01         # krok czasowy
    t = np.arange(0, t_max, dt)

  # Pobudzenie: moment sinusoidalny

    Tm = A * np.sin(2 * np.pi * f * t)

    return Tm