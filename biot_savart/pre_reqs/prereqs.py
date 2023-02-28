import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d import Axes3D

class Curve:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        curve = []
        index = 0
    
        while index < x.shape[0]:
            curve.append([x[index], y[index], z[index]])
            index += 1
    
        self.curve =  np.array(curve)

    def tangent_to_curve(curve, parametarising_variable):
        delta_t = parametarising_variable[1] - parametarising_variable[0]
        tangents = []
    
        for index, element in enumerate(curve):       
            if index < curve.shape[0] - 1 :
                delta_s = curve[index + 1] - curve[index]
                tangents.append(delta_s)           
        
        self.tangents = np.array(tangents)

    def get_curve(self):
        return self.curve

    def get_tangents(self):
        return self.get_tangents

    def plot_curve(self, color = 'blue'):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(self.x, self.y, self.z, color=color)

    def plot_tangent(self, parametarising_variable_value, color):
        point = parametarising_variable_value

        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes(projection='3d')
        ax.plot3D(self.x, self.y, self.z, color=color)
    
        t_0 = t[point]
        origin_and_tangent = [x(t_0), y(t_0), z(t_0), 10*tangents[point][0], 10*tangents[point][1], 10*tangents[point][2]]

        soa = np.array([origin_and_tangent])
        X, Y, Z, U, V, W = zip(*soa)

        ax.quiver(X, Y, Z, U, V, W, color='cyan')
        ax.plot3D(x(t_0), y(t_0), z(t_0), 'o', color='cyan')

        ax.set_xlim([-1, 0.5])
        ax.set_ylim([-1, 1.5])
        ax.set_zlim([-1, 8])
        plt.show()



