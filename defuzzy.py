import numpy as np

def integral_point(X, Y):
    solve = 0.0
    for i in range(len(X) - 1):
        d = X[i+1] - X[i]
        h = min(Y[i], Y[i + 1])
        ht = max(Y[i], Y[i + 1]) - h
        solve += h*d + (ht*d)*0.5 
    return solve

def integral(f, a, b):
    dom = np.linspace(a, b, 10000)
    img = [f(i) for i in dom]
    return integral_point(dom, img)

def bisector(f, a, b):
    l, r = a, b
    eps = 1e-4
    while(r - l > eps):
        m = (l + r) * 0.5
        il = integral(f, a, m)
        ir = integral(f, m, b)
        if abs(ir - il) <= eps:
            return m
        elif il < ir:
            l = m
        else:
            r = m
    return r

def centroid(f, a, b):
    s_dfi = 0.0
    s_fi = 0.0
    dom = np.linspace(a, b, 10000)
    for di in dom:
        s_dfi += di * f(di)
        s_fi += f(di)
    return s_dfi/ s_fi

def mean_max(f, a, b):
    return (left_max(f, a, b) + right_max(f, a, b))/2.0

def left_max(f, a, b):
    dom = np.linspace(a, b, 10000)
    img = [f(i) for i in dom]
    max_value = max(img)
    x_max = 0
    eps = 1e-4
    for x in dom:
        if abs(f(x) - max_value) <= eps:
            return x
    return x_max

def right_max(f, a, b):
    dom = np.linspace(a, b, 10000)
    img = [f(i) for i in dom]
    max_value = max(img)
    x_max = 0
    eps = 1e-4
    for x in dom:
        if abs(f(x) - max_value) <= eps:
            x_max = x
    return x_max


if __name__ == "__main__":
    from membership import triangular
    f = triangular(0, 10, 20)
    # print (integral(f, 0.0, 10.0))
    print (bisector(f, 0, 20))
    print(centroid(f, 0, 20))
    print(mean_max(f, 0, 20))
    print(left_max(f, 0, 20))
    print(right_max(f, 0, 20))

  