import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import minimize

class OneEq:
    def __init__(self):
        pass

    def D(self, f, x):
        return f(x)**2

    def solve(self, f, x, init_guess):
        D = self.D(f, x)
        
        res = minimize(D, init_guess)
        return np.array([res])

if __name__ == '__main__':
    eq = OneEq()
    
    def f(x):
        return x + 1

    x = 1
    eq.solve(f, x, 2)
        

