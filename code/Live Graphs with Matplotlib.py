#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# url: https://pythonprogramming.net/live-graphs-matplotlib-tutorial/?completed=/styles-matplotlib-tutorial/

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('seaborn-darkgrid')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    graph_data=open('example.txt', 'r').read()
    lines=graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.scatter(xs,ys)
    # plt.plot([],[],'-',label='liaochengyu',linewidth=2)


if __name__ == '__main__':
    ani=animation.FuncAnimation(fig,animate,interval=1000)
    ax1.set_title('test')
    # plt.legend()
    plt.show()
