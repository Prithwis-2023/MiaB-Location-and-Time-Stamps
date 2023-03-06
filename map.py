from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

fig.set_facecolor('black')
ax.set_facecolor('black') 
ax.grid(False) 
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False

# points
z_galc = np.repeat(0, 1000)
x_galc = np.repeat(0, 1000) 
y_galc = np.linspace(start=0.0, stop=8.0, num=1000) 

ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')

# plot
ax.plot(x_galc, y_galc, z_galc, c='white',label=r'Sun to Gal. Center')
plt.show()