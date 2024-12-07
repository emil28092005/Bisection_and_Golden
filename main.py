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
    
    x_min = (a + b) / 2.0
    f_min = f_golden(x_min)
    return x_min, f_min

def f_gradient(x):
    return -x**2 + 4*x + 1

def f_prime(x):
    return -2*x + 4

def gradient_ascent(x0, alpha, N):
    x = x0
    for _ in range(N):
        x = x + alpha * f_prime(x)
    return x, f_gradient(x)

if __name__ == "__main__":
    a, b = 1, 2
    eps = 1e-6
    root = bisection_method(a, b, eps)
    print("Task 1: Bisection Method")
    print(f"Approximate root: {root}, f(root) = {f_bisection(root)}")

    a_g, b_g = 0, 5
    eps_g = 1e-4
    x_min, f_min = golden_section_search(a_g, b_g, eps_g)
    print("\nTask 2: Golden Section Search")
    print(f"Approximate x_min: {x_min}, f(x_min) = {f_min}")

    x0 = 0
    alpha = 0.1
    N = 100
    x_max, f_max = gradient_ascent(x0, alpha, N)
    print("\nTask 3: Gradient Ascent Method")
    print(f"Approximate x_max: {x_max}, f(x_max) = {f_max}")
