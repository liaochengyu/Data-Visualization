#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# url: https://pythonprogramming.net/colors-fills-matplotlib-tutorial/?completed=/unix-time-matplotlib-tutorial/

import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data():
    fig=plt.figure()
    ax1=plt.subplot2grid((1,1),(0,0))
    # about subplot2grid method using direction: https://morvanzhou.github.io/tutorials/data-manipulation/plt/4-2-subplot2/

    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
        # if 'values' not in line:
            stock_data.append(line)

    # return stock_data

# def main():
    date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(stock_data,
                                      delimiter=',',
                                      unpack=True,
                                      # %Y = full year. 2015
                                      # %y = partial year 15
                                      # %m = number month
                                      # %d = number day
                                      # %H = hours
                                      # %M = minutes
                                      # %S = seconds
                                      # 12-06-2014
                                      # %m-%d-%Y
                                      converters={0: bytespdate2num('%Y-%m-%d')})
    # plt.plot_date(date, closep,'-', label='Close Price',color='b')
    # plt.plot_date(date, openp,'-', label='Open Price',color='r')
    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # dateconv=np.vectorize(dt.datetime.fromtimestamp)
    # date=dateconv(date)

    ax1.plot_date(date,closep,'-',label='Close price')
    ax1.fill_between(date, closep[0], closep,where=(closep > closep[0]), facecolor='g', alpha=0.5)
    ax1.fill_between(date, closep[0], closep,where=(closep < closep[0]), facecolor='r', alpha=0.5)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.set_xlabel('date')
    ax1.set_ylabel('price')
    # ax1.xaxis.label.set_lable_text('date')
    # ax1.yaxis.label.set_lable_text('price')
    ax1.xaxis.label.set_color('c')
    ax1.yaxis.label.set_color('r')
    ax1.plot([],[],linewidth=5,label='loss',color='g',alpha=0.5)
    ax1.plot([],[],linewidth=5,label='gian',color='r',alpha=0.5)

    # ax1.set_yticks([0,25,50,75])

    ax1.grid(True)
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.subplots_adjust(left=0.09,bottom=0.20,right=0.94,top=0.90,wspace=0.2,hspace=0)
    plt.show()

if __name__ == '__main__':
    graph_data()
