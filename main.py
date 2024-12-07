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
