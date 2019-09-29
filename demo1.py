#!/usr/bin/env python3
# -*- coding: utf-8 -*-




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






list = [4, 2, 3, 4, 5, 7, 8, 53, 3, 4, 6, 8, 3, 2, 2]

print([i for i in list if i > 4])

g = lambda x: x+1

print(g(10))