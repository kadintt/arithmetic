#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def test(arr):

    greater = [i for i in arr if i > 3]

    return greater






def printTest(item):
    print("%s\n" % (item))




def findLessest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def choseShort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest_index = findLessest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


def find(arr):

    # 设置基线条件
    if len(arr) < 2:
        return arr
    else:
        proive = arr[0]
        lessest = [i for i in arr[1:] if i <= proive]
        greatest = [i for i in arr[1:] if i > proive]

        return find(lessest) + [proive] + find(greatest)


# list = [4, 2, 3, 4, 5, 7, 8, 53, 3, 4, 6, 8, 3, 2, 2]

# print(choseShort(list))


def fib(N):
    if N < 2:return N;

    F = [0,1]
    i = 2

    while i < N:
        F.append(F[i-1] + F[i-2])
        i += 1
    return F[i-1] + F[i-2]


# print(fib(8))



from functools import wraps

def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r,%r)->%r'%(func.__name__, args, kwargs, result))
        return result
    return wrapper


@tracer
def fibonacci(n):
    if n in (0, 1):
        return n
    return (fibonacci(n - 1) + fibonacci(n - 2))




list_num = [4, 2, 3, 4, 5, 7, 8, 53, 3, 4, 6, 8, 3, 2, 2]

print([i for i in list_num if i > 4])

g = lambda x: x+1

print(g(10))


class Rectangle(object):
    # def __init__(self):
    #     # self.width = 10
    #     # self.height = 20
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('宽度必须是整数才行')
        if value < 0 or value > 100:
            raise ValueError('宽度必须在0-100之间')
        self._width = value



r=Rectangle()
r.width = 99

print('width is -> %s' % r.width)


def f(a):
    return a*a

def add(a ,b):
    return a*10 + b

if __name__ == '__main__':

    cards = ['w', '3', '4', '8', '2', '2', '2', '3', '2', '3', '4']
    cards.sort(key=lambda ch: '34567890JQKA2wW'.index(ch))
    r = map(f, [1, 2, 2, 3])
    l = list(r)

    result = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(l)
    print(result)
    # print(cards)
    #
    # print(fibonacci(5))
    # print(fibonacci)
    # print('help:')
    # help(fibonacci)