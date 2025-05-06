def rk4(f,t,y,h):  
    k1 = h*f(t,y)
    k2 = h*f(t+h/2, y+k1/2)
    k3 = h*f(t+h/2, y+k2/2)
    k4 = h*f(t+h, y+k3)
    dy = (k1+2*k2+2*k3+k4)/6
    y_next = y+dy 
    return y_next