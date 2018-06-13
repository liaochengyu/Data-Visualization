#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# url: https://pythonprogramming.net/subplot2grid-add_subplot-matplotlib-tutorial/

import matplotlib.pyplot as plt
import random
from matplotlib import style

style.use('fivethirtyeight')

fig=plt.figure()

def create_plots():
    xs=[]
    ys=[]
    for i in range(1,10):
        x=i
        y=random.randrange(10)
        xs.append(x)
        ys.append(y)
    return xs, ys

if __name__ == '__main__':
    # reference the method subplot2grid
    x,y=create_plots()
    ax1=fig.add_subplot(211)
    ax2=fig.add_subplot(212)
    ax1.plot(x,y)
    ax2.plot(x,y)
    plt.show()
