import math

def f_bisection(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection_method(a, b, eps):
    fa = f_bisection(a)
    fb = f_bisection(b)
    if fa * fb > 0:
        raise ValueError("f(a)*f(b) > 0. No guarantee that a root exists in the interval [a,b].")
    
    while True:
        c = (a + b) / 2.0
        fc = f_bisection(c)
        if abs(fc) < eps:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

def f_golden(x):
    return (x - 2)**2 + 3

def golden_section_search(a, b, eps):
    phi = (1 + math.sqrt(5)) / 2.0
    resphi = 2 - phi
    c = a + resphi * (b - a)
    d = b - resphi * (b - a)
    fc = f_golden(c)
    fd = f_golden(d)

    while (b - a) > eps:
        if fc < fd:
            b = d
            d = c
            fd = fc
            c = a + resphi * (b - a)
            fc = f_golden(c)
        else:
            a = c
            c = d
            fc = fd
            d = b - resphi * (b - a)
            fd = f_golden(d)
