import numpy as np
import matplotlib.pyplot as plt
from debug import debug

debug.on()


def step(n):
    div_left = n % 2
    if div_left == 0:
        return n / 2
    elif div_left == 1:
        return 3*n + 1


def graph_calculate(start_n):
    target = start_n
    logged = [target]
    while target > 1:
        target = step(target)
        logged.append(target)

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('scroll_event',on_scroll)
    plt.plot(logged)
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

