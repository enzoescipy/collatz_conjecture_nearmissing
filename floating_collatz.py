import numpy as np
import matplotlib.pyplot as plt
from debug import debug

debug.on()

def gradial_even(num):
    div_left = num % 2
    if div_left > 1.0:
        div_left -= 1.0
    return div_left


def step(n):
    div_left = gradial_even(n)
    if div_left == 0:
        return n * (0.5) ** (1 - div_left)
    elif div_left == 1:
        return n * (3.0) ** () + 1


def step_legacy(n):
    div_left = n % 2
    if div_left == 0:
        return n / 2
    elif div_left == 1:
        return 3*n + 1


def graph_calculate(start_n):


    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('scroll_event',on_scroll)

    target = start_n
    logged = [target]
    iternum = 0
    while target > 1 and iternum < 1000:
        target = step_legacy(target)
        logged.append(target)
        iternum += 1

    plt.scatter(range(1,len(logged) + 1),logged)

    target = start_n
    logged = [target]
    while target > 1 and iternum < 1000:
        target = step(target)
        logged.append(target)
        iternum += 1

    plt.scatter(range(1,len(logged) + 1),logged)

    plt.draw()

current_n = 1

def on_scroll(event):
    plt.close()

    global current_n
    if event.button == 'up':
        current_n += 1
    elif event.button == 'down':
        current_n -= 1
    
    debug.dprint(current_n)

    graph_calculate(current_n)



plt.ion()
graph_calculate(current_n)

while True :
    plt.pause(1)

