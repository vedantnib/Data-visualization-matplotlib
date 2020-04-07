from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
#we create a figure instance which provides an empty canvas.
fig = plt.figure()
#The add_axes() method requires a list object of 4 elements corresponding to left, bottom, width and height of the figure. Each number must be between 0 and 1
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()