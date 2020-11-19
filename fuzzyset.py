import numpy as np
import matplotlib.pyplot as plt

def triangular( a, b, c):
    def f(x):
        if x < a:
            return 0
        elif a <= x and x <= b:
            return 1. * (x - a)/ (b - a)
        elif b <= x and x <= c:
            return 1. * (c - x)/(c - b)
        else:
            return 0
    return f

def trapezoidal(a, b, c, d):
    def f(x):
        if x <= a or x >= d:
            return 0
        if x >= b and x <= c:
            return 1
        if x >= a and x <= b:
            return 1. * (x - a) / (b - a)
        return 1. * (d - x) / (d - c)
    return f

def corte(umbral):
    def f(x):
        return umbral
    return f

def union(f, g):
    def wrapper(x):
        return max(f(x), g(x))
    return wrapper

def intersection(f, g):
    def wrapper(x):
        return min(f(x), g(x))
    return wrapper





if __name__ == "__main__":
    print("hello")
    dom = np.linspace(0, 100, 10000)
    f1 = triangular(10, 20, 30)
    # f1 = trapezoidal(10, 20, 30, 40)
    y1 = [f1(i) for i in dom]

    f2 = triangular(15, 30, 45)
    # f2 = trapezoidal(45, 55, 64, 75)
    y2 = [f2(i) for i in dom]

    # f3 = triangular(25, 35, 45)
    f3 = trapezoidal(15, 40, 60, 85)
    y3 = [f3(i) for i in dom]

    f2 = corte(0.5)
    u = intersection(f1, f2)
    yu = [u(i) for i in dom]
   

    fig, axs = plt.subplots(1,1)

    axs.plot(dom, yu, "b:", label = "f1")
    axs.plot(dom, y1, "r:", label = "f2")
    axs.plot(dom, y2, "g:", label = "f3")
    axs.legend()
    plt.show()

    
    

  
   
  