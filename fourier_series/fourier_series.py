import numpy as np
import matplotlib.pyplot as plt

L = 1
x = np.arange(0, (1/3)*L,0.000001)
func = 0.5*x


a_0 = (1/L)*(np.cumsum(func)* (x[1] - x[0]))[-1]
a_0 = np.round(a_0, 5)

def A_m(m):
    return (1/L)*((np.cumsum(func*np.cos((m*np.pi*x)/L)) * (x[1] - x[0]))[-1])

def B_m(m):
    return (1/L)*((np.cumsum(func*np.sin((m*np.pi*x)/L)) * (x[1] - x[0]))[-1])

def fourier_app(n):
    func_cos = 0
    for i in range(1, n+1):
        func_cos += A_m(i)*np.cos((i*x*np.pi)/L)

    func_sin = 0
    for i in range(1, n+1):
        func_sin += B_m(i)*np.sin((i*x*np.pi)/L)

    fourier_app = func_cos + func_sin
    fourier_app += a_0/2

    return fourier_app

n = int(input('enter n: '))
fourier_app = fourier_app(n)

plt.plot(x, fourier_app, color='green', label = 'fourier approximation')
plt.plot(x,func, color='red', label='orginal function')
plt.xlabel = 'x'
plt.ylabel = 'y'
plt.grid()
plt.legend(loc='upper left')
plt.show()
