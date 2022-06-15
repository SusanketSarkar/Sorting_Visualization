import time
from colors import *

def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap
    heapify(arr, n, largest)
 
def heap_sort(nums, drawData, timee):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i] # swap
        heapify(nums, i, 0)
        drawData(nums, [DARK_YELLOW if x==i else DARK_GREEN for x in range(len(nums))] )
        time.sleep(timee)
    drawData(nums, [DARK_GREEN for x in range(len(nums))])