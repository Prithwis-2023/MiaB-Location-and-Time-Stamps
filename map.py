from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import math
import pandas as pd

fig = plt.figure()
ax = plt.axes(projection='3d')


fig.set_facecolor('black')
ax.set_facecolor('black') 
ax.grid(False) 
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False

def plot_gc(ID, l, b, dist_Sun, points):
    z_coor = np.linspace(0, dist_Sun, num = points)
    #x_coor = np.repeat(0, points)
    x_coor =  math.cos(b * (math.pi / 180)) * math.sin(l * (math.pi / 180)) * abs(z_coor)
    y_coor = np.repeat(0, points)
    y_coor = math.cos(b * (math.pi / 180)) * math.cos(l * (math.pi / 180)) * abs(z_coor)
    #y_coor = math.tan(b*(math.pi/180)) * z_coor #first converted to radians 
    #x_coor = math.tan(l*(math.pi/180)) * y_coor #first converted to radians
    ax.plot(x_coor, y_coor, z_coor, label = r'Sun to NGC {}'.format(ID), linewidth=2)
        
# points for Sun to Galactic Center
z_galc = np.repeat(0, 1000)
x_galc = np.repeat(0, 1000) 
y_galc = np.linspace(start=0.0, stop=8.0, num=1000) 

ax.plot(x_galc, y_galc, z_galc, label=r'Sun to Gal. Center', linewidth=2)

plot_gc(104, 305.89, -44.89, -4.5, 1000)  # NGC 104 (47 Tucanae)
plot_gc(5139, 309.10, 14.97, 5.2, 1000) # NGC 5139 (Omega Centauri)
plot_gc(6441, 353.53, -5.01, -11.6, 1000) # NGC 6441
plot_gc(6440, 7.73, 3.80, 8.5, 1000)      # NGC 6440 
plot_gc(6402, 21.32, 14.81, 9.3, 1000)    # NGC 6402
plot_gc(7089, 53.37, -35.77, -11.5, 1000) # NGC 7089
plot_gc(7078, 65.01, -27.31, -10.4, 1000) # NGC 7078
plot_gc(1851, 244.51, -35.03, -12.1, 1000) # NGC 1851

color = 'white' # specifying color for label of axes

ax.set_xlabel('X-Axis', c=color)
ax.set_ylabel('Y-Axis', c=color)
ax.set_zlabel('Z-Axis', c=color)

plt.legend()
plt.savefig('3d-map.png', dpi = 1000)
plt.show()
