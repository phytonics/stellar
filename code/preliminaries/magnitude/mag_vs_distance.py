# Plot of Magnitude as it varies with Distance

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib import image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

plt.rcParams['axes.facecolor']='black'
plt.rcParams['savefig.facecolor']='black'

msun = -26.74
Rsun = 1.495978707e11

R = 10**np.linspace(0, 12, 100000)

m = msun + 5 * (np.log(R / Rsun)/np.log(10))

xspecial = [Rsun]
yspecial = [msun]

# Initialize Subplots
fig, ax = plt.subplots(figsize=(10, 10), facecolor = "black")


# Special Earth Location
im = image.imread("earth.png")
ax.imshow(im, aspect='auto', extent=(xspecial[0]-1e10, xspecial[0]+1e10, yspecial[0]-1, yspecial[0]+1))
ax.text(xspecial[0], yspecial[0]+2, "At Earth", color='white')

# Plot Axes
ax.plot(R, m, c = "white", alpha = 0.8)

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

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
ax.set_xlabel('R', size = 14, x = 1.02)
ax.set_ylabel('m', size = 14, rotation = 0, y = 1.02, x = 0)




# Draw arrows
arrow_fmt = dict(markersize=4, color='white', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

plt.show()
