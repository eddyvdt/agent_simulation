##!python3
# ==================================================
# Computational Society for Bocconi Students project
# ==================================================
#
# Plotting functions for simulation.py where the rest is contained

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.lines as lines

def plot_agent(x, y, ax):
    
    circle = Circle([x,y], 0.05, edgecolor = 'r', facecolor = 'r', zorder=8)
    ax.add_artist(circle)

    edge = Circle([x,y], 0.05, facecolor = 'None', edgecolor = 'crimson', zorder = 8)
    ax.add_artist(edge)

