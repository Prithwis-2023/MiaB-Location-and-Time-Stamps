from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

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
y_tuc = -0.99616762856204204472570620423053*z_tuc #for B (galactic latitude)
x_tuc = -1.3819535514372218087543204143034*y_tuc  #for L (galactic longitude)


#points for Sun to NGC 5139
z_5139 = np.linspace(0, 5.2, num=1000)
x_5139 = np.repeat(0, 1000)
y_5139 = 0.26738807962645813747654902490062*z_5139 #for B
x_5139 = -1.2304997241409141008745933370653*y_5139 #for L

#points for Sun to NGC 6441
z_6441 = np.linspace(0, -3.9, num=1000)
x_6441 = np.repeat(0, 1000)
y_6441 = -0.08766453505988449896723384277002*z_6441 #for B
x_6441 = -0.11340524411253067779382016726172*y_6441 #for L

ax.set_xlabel('X-Axis', c='black')
ax.set_ylabel('Y-Axis', c='black')
ax.set_zlabel('Z-Axis', c='black')

# plot
ax.plot(x_galc, y_galc, z_galc, label=r'Sun to Gal. Center')
ax.plot(x_tuc, y_tuc, z_tuc, label=r'Sun to 47 Tucanae')
ax.plot(x_5139, y_5139, z_5139, label=r'Sun to NGC 5139')
ax.plot(x_6441, y_6441, z_6441, label=r'Sun to NGC 6441')
plt.legend()
plt.show()