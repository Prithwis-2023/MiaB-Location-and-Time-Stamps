from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
'''
fig.set_facecolor('black')
ax.set_facecolor('black') 
ax.grid(True) 
ax.w_xaxis.pane.fill = False
ax.w_yaxis.pane.fill = False
ax.w_zaxis.pane.fill = False
'''
# points for Sun to Galactic Center
z_galc = np.repeat(0, 1000)
x_galc = np.repeat(0, 1000) 
y_galc = np.linspace(start=0.0, stop=8.0, num=1000) 

# points for Sun to 47 Tuc
z_tuc = np.linspace(0, -4.5, num=1000)
x_tuc = np.repeat(0, 1000)
y_tuc = 0.99616762856204204472570620423053*z_tuc
x_tuc = 1.3819535514372218087543204143034*z_tuc


ax.set_xlabel('X-Axis', c='black')
ax.set_ylabel('Y-Axis', c='black')
ax.set_zlabel('Z-Axis', c='black')

# plot
ax.plot(x_galc, y_galc, z_galc, c='black', label=r'Sun to Gal. Center')
ax.plot(x_tuc, y_tuc, z_tuc, c='black', label=r'Sun to 47 Tucanae')
plt.show()