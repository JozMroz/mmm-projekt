def euler_method(h, y, t, f):
    dy = h*f(t, y)
    y_next = y + dy
    return y_next
