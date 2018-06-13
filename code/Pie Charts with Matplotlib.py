#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# url:https://pythonprogramming.net/pie-chart-matplotlib-tutorial/?completed=/stack-plot-matplotlib-tutorial/

# bar charts
import matplotlib.pyplot as plt
slices=[7,2,2,13]
activities=['sleeping', 'eating', 'working', 'playing']
colors=['c','m','r','b']


# sleeping = [7,8,6,11,7]
# eating = [2,3,4,3,2]
# working = [7,8,7,2,2]
# playing = [8,5,7,8,13]

# plt.plot([],[],color='m', label='Sleeping', linewidth=5)
# plt.plot([],[],color='c', label='Eating', linewidth=5)
# plt.plot([],[],color='r', label='Working', linewidth=5)
# plt.plot([],[],color='k', label='Playing', linewidth=5)

# maker variable reference website：https://matplotlib.org/api/markers_api.html
plt.pie(slices,
    labels=activities,
    colors=colors,
    startangle=45,
    shadow=True,
    explode=(0,0.1,0,0),
    autopct='%1.2f%%')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.zlabel('z')

plt.title('Interesting Graph\nCheck it out')

# plt.legend()
plt.show()
# if __name__=='__main__':
