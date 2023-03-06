import numpy as np
import matplotlib.pyplot as plt
from numpy import prod

x = np.arange(-100000,100000,0.1)
y = np.e**x

def differentiate(x, y):
    dy_dx = np.gradient(y, x)
    return dy_dx

def n_th_ord_derivative(n, y):
    c = 0
    y_n_x = y

    while c < n:        
        y_n_x = differentiate(x, y_n_x)
        
        c += 1
        
    return y_n_x

def index(char, iterable):
    c = 0
    for i in iterable:
        if i.round(4) == char:
            return c
        c += 1

def y_x_0(x_0,x ,y):
    i = index(x_0, x)
    return y[i]


def factorial(n):
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i
    return fact
    

def taylor_app(n, a):
    y_app = np.zeros(x.shape)

    for i in range(0, n):
        y_app = y_app + (y_x_0(a, x, n_th_ord_derivative(i, y))*((x-a)**i))/factorial(i)
    return y_app

if __name__=='__main__':
    y_app = taylor_app(22, 0)

    plt.plot(x,y_app, color='black', lw =2, ms=3, label='function_approximation')

    plt.ylim([-2, 2])   
    plt.xlim([-13, 8])   
    plt.grid()
    plt.legend()
    plt.show()
