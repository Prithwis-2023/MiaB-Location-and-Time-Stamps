import matplotlib.pyplot as plt
import numpy as np
names = ["NGC 5139", "NGC 6715", "NGC 6441", "NGC 104", "NGC 2419", "NGC 6388", "NGC 2808", "NGC 7078", "NGC 6266", "NGC 6273", "NGC 6402", "NGC 7089"]
m_v = [-10.26, -9.98, -9.63, -9.42, -9.42, -9.41, -9.39, -9.19, -9.18, -9.13, -9.10, -9.03]
plt.xlabel("Globular Clusters")
plt.ylabel("Absolute Visual Magnitude")
plt.scatter(names, m_v)
plt.savefig('2.png', dpi=500)
