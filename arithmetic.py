#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import numpy as np

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr




def quickSort(array):
    # print("quickSort")
#     基线条件
    if len(array) < 2:
        return array
    else:
        # 递归条件
        pivot = array[0]
        # 由所有小于等于基准值的元素组成的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 用所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)


my_list = [1,3,4,6,8,24,34,222,434,1244]

find = [12,123,123,12,2,1,23,123,123,1231,188]

index = binary_search(my_list, 24)

# new_list = selectionSort(find)
# print(index)
print(find)
print(quickSort(find))


def short(arr=[]):
    arr.sort()
    last = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if last == arr[i]:
            del arr[i]
        else:
            last = arr[i]
            print(arr)

def npTest():
    # a = np.arange([24, 3])
    # print(a.ndim)

    # b = a.reshape(2 ,1)

    # print(b)

    c = np.array([[1, 2, 3], [4, 5, 6]])
    # c.shape = (3, 2)
    b = c.reshape(3, 2)
    print(b)


    d = np.array([1, 2, 3, 4, 5, 6, 7])
    print(d.flags)

if __name__ == '__main__':
    npTest()
    # arr = [1, 34, 34, 2, 3, 52, 66, 33, 2, 1, 22, 4, 44, 22, 33, 32, 34, 66]
    # short(arr)
    # del arr[2]
    # print(arr)