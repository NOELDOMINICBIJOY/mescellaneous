# importing all necessary modules

import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
import scienceplots

plt.style.use(['science', 'notebook','grid'])
plt.style.use(['science', 'notebook','grid', 'dark_background'])
plt.style.use(['science', 'notebook','grid'])

# defing our function
# if you wish to change the function do it here

x = smp.symbols('x')
sigma = 0.75
amplitude = 2
y = amplitude*smp.exp(-(x**2)/sigma**2)

# defining a function that plots the above defined sympy expression as a matplotlib plot

def plot_smp_func(x, y, title, color = '#00ff00', xlim = (-5, 5), ylim = (-5, 5), xlabel = 'x', ylabel = 'y', grid = True, legend = True):
    
    y_f = smp.lambdify(x, y)    
    x_f = np.linspace(xlim[0], xlim[1], 500)
    
    plt.plot(x_f, y_f(x_f), color = color, label = title)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    if grid:
        plt.grid()
    if legend:
        plt.legend()
        
    plt.show()

# defining a function that returns the nth order derivative of any* mathematical function

def derivative(func, x, n):
    y_n_prime = [func]
    while n > 0:
        y_n_prime.append(smp.diff(y_n_prime[-1], x))
        n -= 1
    return y_n_prime

# defining a function that returns the taylor series of any* mathematical function

def taylor_app(i, func, x, a):
    series = [func]
    n = 0
    
    while i >= 0:
        f_n = derivative(func, x, n)[n]
        f_n_a = f_n.subs(x, a)
        
        ith_approximation = (f_n_a/smp.factorial(n))*(x-a)**n
        series.append(ith_approximation)
        i -= 1
        n += 1
            
    return sum(series[1:])

if __name__ == "__main__":
    x = smp.symbols('x')
    sigma = 0.75
    amplitude = 2
    y = amplitude*smp.exp(-(x**2)/sigma**2)
    plot_smp_func(x, taylor_app(10, y, x, 0), 'taylor_series_expansion')

