#!/usr/bin/env python
# coding: utf-8

# In[1]:


def first_element_pivot_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return first_element_pivot_quicksort(less) + [pivot] + first_element_pivot_quicksort(greater)

def last_element_pivot_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    return last_element_pivot_quicksort(less) + [pivot] + last_element_pivot_quicksort(greater)

def median_of_three_pivot_quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Choose the pivot as the median of the first, middle, and last elements
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    pivot = sorted([first, middle, last])[1]

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return median_of_three_pivot_quicksort(less) + equal + median_of_three_pivot_quicksort(greater)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]

sorted_first_pivot = first_element_pivot_quicksort(arr)
sorted_last_pivot = last_element_pivot_quicksort(arr)
sorted_median_of_three_pivot = median_of_three_pivot_quicksort(arr)

print("First Element Pivot Quicksort:", sorted_first_pivot)
print("Last Element Pivot Quicksort:", sorted_last_pivot)
print("Median-of-Three Pivot Quicksort:", sorted_median_of_three_pivot)


# In[2]:


import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
randomized_quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


# In[ ]:




