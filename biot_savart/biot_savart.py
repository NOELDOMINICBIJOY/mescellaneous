import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
import scienceplots
from prereqs.vecs_and_curves import *
from sklearn.preprocessing import normalize

plt.style.use(['science', 'notebook', 'grid'])

color_of_wire = input("color of wire: ")
color_of_field = input("color_of_field: ")

def create_rs(start, end, steps):
    z = y = x = start
    q = []
    
    while x <= end:
        while y <= end:
            while z <= end:
                q.append([x, y, z])
                z += steps

            z = 0
            y += steps
        y = 0
        x += steps
         
        
    return np.array(q)

r_ps = create_rs(0, 10, 1)

s = smp.symbols('s')
r_dl = Vector(s + 5, 5,5)
r_dl_prime = r_dl.differentiate()


r_p_index = 0
b = []
while r_p_index < len(r_ps):
    r_p = Vector(r_ps[r_p_index][0], r_ps[r_p_index][1], r_ps[r_p_index][2])
    r_p_dl = r_p - r_dl
    
    db = (r_dl_prime.cross(r_p_dl)/(r_p_dl.norm() ** 3))
    db = Vector(db[0], db[1], db[2])
    
    db_f = db.convert_to_function(s)   
    b.append(integrate_function(db_f, [0, 2*np.pi]))
    
    r_p_index += 1

idx = 0
b_m = []

while idx < len(b):
    b_i = []

    for i in b[idx]:
        b_i.append(i[0])
        
    b_m.append(b_i)
    
    idx += 1

def tanh(arr, n):
    return (np.e**(n*arr) - np.e**(-n*arr))/(np.e**(n*arr) + np.e**(-n*arr))

b_m = np.array(b_m)

for i in b_m:
    mag = np.linalg.norm(i)
    i /= mag
    i *= tanh(mag, n = 25)

x_ps = []
for i in r_ps:
    x_ps.append(i[0])
    
y_ps = []
for i in r_ps:
    y_ps.append(i[1])
    
z_ps = []
for i in r_ps:
    z_ps.append(i[2])

x_bm = []
for i in b_m:
    x_bm.append(i[0])
    
y_bm = []
for i in b_m:
    y_bm.append(i[1])
    
z_bm = []
for i in b_m:
    z_bm.append(i[2])


t = np.linspace(0, 2*np.pi, 1000)
wire = Curve(t + 5*np.ones(t.shape),5*np.ones(t.shape), 5*np.ones(t.shape), t)

fig = plt.figure(figsize=(10,10))
ax = fig.gca(projection='3d')

ax.quiver(x_ps, y_ps, z_ps, x_bm, y_bm, z_bm, color = color_of_field, length = 0.5)
ax.plot3D(wire.x, wire.y, wire.z, color=color_of_wire)
ax.set_xlim(-0, 10)
ax.set_ylim(-0, 10)
ax.set_zlim(-0, 10)

plt.show()
