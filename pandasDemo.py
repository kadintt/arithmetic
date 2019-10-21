#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Person(object):

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 18:
            print('未成年人不得进入')
        else:
            print('欢迎归来')



def test1():
    data = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    print(data)

    data1 = {'a': [1, 2, 3], 'b': ['we', 'you', 'they'], 'c': ['btc', 'eos', 'ae']}
    df = DataFrame(data1)
    print(df)


    data2 = Series([222, 11, 21, '22', -1])
    print(data2)

    p = Person()
    p.age = 19

    dic = {'a': 1, 'b': 2, 'c': 'aas'}
    dicSeries = Series(dic)
    print(dicSeries)

    print(dicSeries.index, dicSeries.values)


    index1 = ['a', 'b', 'c', 'd']
    dic1 = {'b': 1, 'c': 1, 'd': 1}


def test2():
    index1 = ['a', 'b', 'c', 'd']
    dic1 = {'b': 1, 'c': 1, 'd': 1}
    data3 = Series(dic1, index=index1)
    # print(data3)
    # print(data3.isnull)
    # print(data3.notnull)
    # print([data3.isnull() == True])

    # data3.index.name = 'abc'
    # data3.name = 'test'
    # print(data3)
    #

    data = {'name' :['BTC', 'ETH', 'EOS'], 'price': [50000, 4000, 150]}
    data = DataFrame(data)
    print(data, data.values, data.index)
    print(['*']*10)
    print(data['name'])
    print(['空格'] * 10)
    print(data.iloc[1])


def pltDemo():
    # x = np.linspace(0, 2*np.pi, 50)
    # plt.plot(x, np.sin(x), 'r-o',  x, np.sin(2*x), 'g--')
    #
    # plt.show()

    x = np.linspace(0, 2 * np.pi, 50)
    plt.subplot(2, 1, 1)  # (行， 列， 活动区)

    plt.plot(x, np.sin(x), 'r')

    plt.subplot(2, 1, 2)

    plt.plot(x, np.cos(x), 'g')

    plt.show()

def scatterDemo():
    x = np.linspace(0, 2 * np.pi, 100)

    y = np.sin(x)

    plt.scatter(x, y)

    plt.show()

def scatterColorDemo():
    x = np.random.rand(1000)
    y = np.random.rand(1000)
    size = np.random.rand(10000) * 50
    colour = np.random.rand(1000)

    plt.scatter(x, y, size, colour)

    plt.colorbar()

    plt.show()


def histTest():
    x = np.random.randn(1000)
    print(x)
    plt.hist(x, 50)
    plt.show()


def legendTest():
    x = np.linspace(0, 2*np.pi, 50)
    plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')

    plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')

    #展示图例
    plt.legend()

    #给x轴添加标签
    plt.xlabel('Rads')

    #给y轴添加标签
    plt.ylabel('Amplitude')

    #添加图形标题
    plt.title('Sin and Cos Waves')


    plt.show()


if __name__ == '__main__':
    #饼图阴影、分裂等属性设置

# labels参数设置每一块的标签；

# labeldistance参数设置标签距离圆心的距离（比例值）

# autopct参数设置比例值小数保留位(%.3f%%)；

# pctdistance参数设置比例值文字距离圆心的距离

# explode参数设置每一块顶点距圆心的长度（比例值,列表）；

# colors参数设置每一块的颜色（列表）；

# shadow参数为布尔值，设置是否绘制阴影

# startangle参数设置饼图起始角度
    x = [11, 22, 33, 44]
    plt.pie(x, labels=['a', 'b', 'c', 'd'])

    plt.show()