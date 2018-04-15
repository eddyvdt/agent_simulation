#!python3
# ==================================================
# Computational Society for Bocconi Students project
# ==================================================
#
# The goal is to simulate a population of agents and their interactions over
# time.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.lines as lines
import simplotting as sp

# SETTINGS OF THE SIMULATION:

settings = dict()

settings['pop_size'] = 10       # number of agents to spawn
settings['time'] = 100          # number of time steps for the simulation

settings['x_min'] = -2.0        # left side of the arena
settings['x_max'] = 2.0         # right side of the arena
settings['y_min'] = -2.0        # lower bound of the arena
settings['y_max'] = 2.0         # upper bound of the arena

# Basic agent class, it only initializes its position and defines nothing else

class agent():
    def __init__(self, settings):
        
        self.x = np.random.uniform(settings['x_min'], settings['x_max'])
        self.y = np.random.uniform(settings['y_min'], settings['y_max'])

# A function to generate as many agents as specified in the settings

def generate(settings):
    agents = []
    for i in range(settings['pop_size']):
        agents.append(agent(settings))

    return agents

# plotting function, its connected to the file simplotting.py that has a specific
# function to plot the agents as red circles, the function down here is more about
# the figure, labels, text and its settings

def plot_frame(settings, agents, time):
    fig, ax = plt.subplots()
    fig.set_size_inches(9.6, 5.4)
    plt.xlim([settings['x_min'], settings['x_max']])
    plt.ylim([settings['y_min'], settings['y_max']])

    for a in agents:
        sp.plot_agent(a.x, a.y, ax)

    ax.set_aspect('equal')

    plt.figtext(0.0025, 0.90, r'T_STEP: '+str(time))
    plt.savefig(str(time)+'.png', dpi=100)

# a simulation function, since as a basis our agents do nothing, this does nothing
# aswell, modify as you wish

def simulate(settings, agents):

    return agents

# simply runs through the simulation and plots at every point in time, note that
# there will be 100 equal plots since nothing has been done until now

def run_simulation(s = settings):
    steps = settings['time']

    agents = generate(settings)

    for t in range(steps):
        agents = simulate(settings, agents)
        plot_frame(settings, agents, t)

    pass
