#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# url:https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/

# bar charts
import matplotlib.pyplot as plt
import csv

x=[]
y=[]

# 语法链接：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000
with open(r'C:\Users\Administrator\Desktop\Tech.csv', 'r') as csvfile:
    # csvlist=csvfile.readlines() # readlines 方法可以一次性的读取所有的文件信息
    plots =list(csv.reader(csvfile, delimiter=','))
    # print(plots [0][0])

    num=1
    # while num<5:
    for row in plots:
        num=num+1
        print(row[0])
        if num>20:
            break


# sleeping = [7,8,6,11,7]
# eating = [2,3,4,3,2]
# working = [7,8,7,2,2]
# playing = [8,5,7,8,13]

# plt.plot([],[],color='m', label='Sleeping', linewidth=5)
# plt.plot([],[],color='c', label='Eating', linewidth=5)
# plt.plot([],[],color='r', label='Working', linewidth=5)
# plt.plot([],[],color='k', label='Playing', linewidth=5)

# maker variable reference website：https://matplotlib.org/api/markers_api.html
# plt.pie(slices,
#     labels=activities,
#     colors=colors,
#     startangle=45,
#     shadow=True,
#     explode=(0,0.1,0,0),
#     autopct='%1.2f%%')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.zlabel('z')

# plt.title('Interesting Graph\nCheck it out')

# plt.legend()
# plt.show()
# if __name__=='__main__':
