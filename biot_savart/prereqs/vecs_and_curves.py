import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import sympy as smp
from scipy.integrate import quad_vec

plt.style.use(['science', 'notebook', 'dark_background'])
plt.style.use(['science', 'notebook', 'dark_background', 'grid'])
plt.style.use(['science', 'notebook', 'dark_background'])

class Vector:
    def __init__(self, x, y, z):
        """here x, y and z are sympy symbols"""

        self.x = x
        self.y = y
        self.z = z

        self.vector = smp.Matrix([self.x, self.y, self.z])
    
    def differentiate(self):
        return smp.diff(self.vector)

    def norm(self):
        return self.vector.norm()

    def convert_to_function(self, parameterising_variable):
        function_f = smp.lambdify([parameterising_variable], self.vector)
        return function_f

    def __add__(self, v2):
        return self.vector + v2.vector

    def __sub__(self, v2):
        return self.vector - v2.vector
    
    def dot(self, v2):
        return self.vector.dot(v2.vector)

    def cross(self, v2):
        return self.vector.cross(v2.vector)
    
class Curve:
    def __init__(self, x, y, z, parametarising_variable):
        self.t = parametarising_variable
        self.x = x
        self.y = y
        self.z = z
        
        curve = []
        index = 0

        while index < x.shape[0]:
            curve.append([self.x[index],self.y[index], self.z[index]])
            index += 1

        self.curve = np.array(curve)

    def plot_curve(self, figsize = (10, 10), color = '#51ff00', show_plot = False):
        fig = plt.figure(figsize = figsize)
        ax = plt.axes(projection = '3d')
        
        ax.plot3D(self.x, self.y, self.z, color = color)
        if show_plot:
            plt.show


def integrate_function(function, bounds):
    return quad_vec(function, bounds[0], bounds[1])[0]

if __name__ == "__main__":
    s, ds = smp.symbols('s ds')

    r_dl = Vector(smp.cos(s), smp.sin(s), 0)
    r_dl_prime = r_dl.differentiate()

    r_p = Vector(0, 0, 0)
    r_p_dl = r_p - r_dl

    db = (r_dl_prime.cross(r_p_dl)/(r_p_dl.norm() ** 3))
    db = Vector(db[0], db[1], db[2])

    db_f = db.convert_to_function(s)   
    print(integrate_function(db_f, [0, 2*np.pi]))
    

