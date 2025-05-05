import numpy as np

def euler_method(h, y0, t0, t_k, f):
    
    t = np.arange(t0, t_k + h, h)
    y = np.zeros(len(t))
    y[0] = y0 # Initial Condition
    
    for i in range(0, len(t) - 1):
        y[i + 1] = y[i] + h*f(t[i], y[i])
    
return y,t