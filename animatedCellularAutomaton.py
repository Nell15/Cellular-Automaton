"""
animatedCellularAutomaton.py
@author: TRUONG - Nell
"""

###----- Imports -----

from cellularAutomaton import *
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter

###----- Important -----
# This code has to be in the same folder as cellularAutomaton.py to work.
# Please read README.md for more details.

###----- SETUP -----

# This is where your rule will be selected. You may change it tou your liking.
# You can name one that is specified in the ruleset section of cellularAutomaton.py
# or you can add your own (cf README for details)
# Here is an example :

rule = rule57

# This is where your starting line will be selected. You may change it tou your liking.
# Here are two examples :

# l = [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0]
l = [1] * 50 + [0] + [1] * 50

image = [l]

# Number of generations you want to create. You may change this value to your liking.
# The final animation will have a number of line correspongding to the number of generations.

n = 100

###----- ANIMATION -----

fig = plt.figure()
data = image + ([[1] * len(l)] * (n))
im = plt.imshow(data, cmap = 'gray', clim = (0, 1))

def init():
    im.set_data(image + ([[1] * len(l)] * (n)))

def animate(i):
    data[i + 1] = nextGen(rule, data[i])
    im.set_data(data)
    return im

###----- Results display -----

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n, interval=50)
plt.show()

###----- GIF Save -----

# Uncomment the next to lines to generate and save a gif of the animation.
# By default, the .gif will be saved in the same folder the code is in.

# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n, interval=50)
# anim.save('animation.gif', writer=PillowWriter(fps=25))