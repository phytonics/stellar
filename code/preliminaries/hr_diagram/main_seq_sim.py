# Plot of Main Sequence Stars

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib import image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

plt.rcParams['axes.facecolor']='black'
plt.rcParams['savefig.facecolor']='black'

T = np.linspace(5000, 10000, 1000000)
sigma = 5.67e-8
R = np.sort(2**np.random.normal(0, 0.5, 1000000)) * 6.9634e9


L = np.pi * R**2 * sigma * T**4

# Initialize Subplots
fig, ax = plt.subplots(figsize=(10, 10), facecolor = "black")

# Plot Axes
ax.plot(T, L, c = "white", alpha = 0.8)



# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set Everything as White
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')



# Create 'x' and 'y' labels
ax.set_xlabel('T', size = 14, x = 1.02)
ax.set_ylabel('L', size = 14, rotation = 0, y = 1.02, x = 0)
ax.set(xlim = (5000, 10500), ylim=(1e25, 1e31))
ax.invert_xaxis()
ax.set_yscale('log')

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position(('data', 1e25))
ax.spines['left'].set_position(('data', 10500))

# Draw arrows
arrow_fmt = dict(markersize=4, color='white', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)


ax.text(7500, 1e29, "$L = Ae\sigma T^4$", color = "white", fontsize=20)

plt.show()
