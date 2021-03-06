#!python
from utils import time_it

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)

@time_it
def linear_search_iterative(array, item):
    # loop over all array values until item is found
    # Time complexity: O(n)
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

@time_it
def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # Time complexity: O(n)
    if index == len(array):
        return None
    if item == array[index]:
        return index
    return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)

# @time_it
def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # Time complexity: O(logn)
    # low = 0
    # high = len(array)
    # mid = int((low+high)/2)
    # while high > low:
    #     mid = int((low+high)/2)
    #     if array[mid] == item:
    #         return mid
    #     elif array[mid-1] == item:
    #         return mid-1
    #     elif array[mid] > item:
    #         high = mid-1
    #     elif array[mid] < item:
    #         low = mid+1
    # return None
    low = 0
    high = len(array)
    mid = int((low+high)/2)
    while high > low:
        mid = int((low+high)/2)
        if array[mid] == item:
            return True
        elif array[mid-1] == item:
            return True
        elif array[mid+1] == item:
            return True
        elif array[mid] > item:
            high = mid+1
        elif array[mid] < item:
            low = mid-1
    return False
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


# @time_it
def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # Time complexity: O(logn)
    # try:
    #     if left > right or left == right:
    #         return None
    #     mid = int((left+right)/2)
    #     if array[mid] == item:
    #         return mid
    #     elif array[mid-1] == item:
    #         return mid-1
    #     elif array[mid] > item:
    #         return binary_search_recursive(array, item, left, mid-1)
    #     elif array[mid] < item:
    #         return binary_search_recursive(array, item, mid+1, right)
    # except:
    #     return binary_search_recursive(array, item, 0, len(array))
    try:
        if left >= right:
            return False
        mid = int((left+right)/2)
        if array[mid] == item:
            return True
        elif array[mid-1] == item:
            return True
        elif array[mid+1] == item:
            return True
        elif array[mid] > item:
            return binary_search_recursive(array, item, left, mid-1)
        elif array[mid] < item:
            return binary_search_recursive(array, item, mid+1, right)
    except:
        return binary_search_recursive(array, item, 0, len(array))
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

def main():
    words = list(open("/usr/share/dict/words","r"))
    names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
    # print(binary_search(names, 'Winnie'))
    # linear_search(words, 'the')
    # print(words[len(words)-1])
    # linear_search(words, 'the')
    binary_search(words, 'Winnie')
    binary_search(words, 'Zyzzogeton')

if __name__ == '__main__':
    main()
