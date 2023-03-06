import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import time

plt.style.use(['science', 'notebook', 'dark_background', 'grid'])

L = 10

_ = np.linspace(-L, L,100)
theta, theta_dot = np.meshgrid(_,_)

m = 1
k = 0

theta_dot_ = theta_dot
theta_ddot_ = -k*theta_dot - m*np.sin(theta)

magnitude = np.sqrt(theta_dot_**2 + theta_ddot_**2)

X = theta
Y = theta_dot
U = theta_dot_
V = theta_ddot_

fig, axes = plt.subplots(1,2,figsize=(20,10))

ax = axes[0]
lw = 5*magnitude / magnitude.max()
ax.streamplot(X, Y, U, V, linewidth=lw, color=magnitude)
ax = axes[1]

t = np.arange(-L, L, 1)
td = t

seed_points = []
for i in t:
    for j in td:
        seed_points.append([i, j])
        
seed_points = np.array(seed_points)

ax.streamplot(X, Y, U, V, color=U, linewidth=2,
                      cmap='hot', start_points=seed_points)
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)

plt.savefig('visualising_hamiltonian_flow.png')
plt.show()
