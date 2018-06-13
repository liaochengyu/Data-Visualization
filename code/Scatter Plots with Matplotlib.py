#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# url: https://pythonprogramming.net/scatter-plot-matplotlib-tutorial/

# bar charts
import matplotlib.pyplot as plt
x=list(range(1,9))
y=[5,2,4,2,1,4,5,2]
z=[5,2,4,2,1,4,5,2]

# maker 参数选择参考链接：https://matplotlib.org/api/markers_api.html
plt.scatter(x, y, label='skitscat', color='k', marker='o')


plt.xlabel('x')
plt.ylabel('y')
# plt.zlabel('z')

plt.title('Interesting Graph\nCheck it out')

plt.legend()
plt.show()
# if __name__=='__main__':
