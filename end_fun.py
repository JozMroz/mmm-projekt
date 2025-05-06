import numpy as np

def end_fun(t, y, dt, Tm_tab, Jeq, beq):
    i = int(t / dt)
    if i >= len(Tm_tab):
        Tm = Tm_tab[-1]
    else:
        Tm = Tm_tab[i]
    w = y[1]
    dphi = w
    dw = (Tm - beq * w) / Jeq
    return np.array([dphi, dw])