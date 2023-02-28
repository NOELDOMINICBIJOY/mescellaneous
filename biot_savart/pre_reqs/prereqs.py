import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


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

    def tangent_to_curve(self):
        delta_t = self.t[1] - self.t[0]
        tangents = []

        for index, element in enumerate(self.curve):
            if index < self.curve.shape[0] - 1:
                delta_s = self.curve[index + 1] - self.curve[index]
                tangents.append(delta_s)

        self.tangents = np.array(tangents)
        return self.tangents

    def plot_curve(self, figsize = (10, 10), color = '#51ff00', show_plot = False):
        fig = plt.figure(figsize = figsize)
        ax = plt.axes(projection = '3d')
        
        ax.plot3D(self.x, self.y, self.z, color = color)
        if show_plot:
            plt.show

    def plot_tangent(self, x, y, z, parametarising_variable_value, figsize, color_of_curve, color_of_tangent, x_lim, y_lim, z_lim, show_plot = False, scaling_factor = 10):
        """parametarising_variable_value to be between defining bounds of parametarising_variable"""
        """x, y, z are function unlike the arrays when used in defining the curve"""

        t_0 = self.t[parametarising_variable_value]

        fig = plt.figure(figsize = figsize)
        ax = plt.axes(projection = '3d')
        
        ax.plot3D(self.x, self.y, self.z, color = color_of_curve)

        origins_and_tangents = [x(t_0), y(t_0), z(t_0),scaling_factor*self.tangents[parametarising_variable_value][0], scaling_factor*self.tangents[parametarising_variable_value][1], scaling_factor*self.tangents[parametarising_variable_value][2]]
        soa = np.array([origins_and_tangents])
        X, Y, Z, U, V, W = zip(*soa)
        
        ax.quiver(X, Y, Z, U, V, W, color = color_of_tangent)
        ax.plot3D(x(t_0), y(t_0), z(t_0), 'o', color = color_of_tangent)

        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)
        ax.set_zlim(z_lim)
    
        if show_plot:
            plt.show
