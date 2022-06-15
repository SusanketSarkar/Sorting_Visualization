from re import A
import time
from colors import *
def selection_sort(nums, drawData, timee):
    for idx in range(len(nums)):
        min_idx = idx
        for j in range( idx +1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        a, b = nums[idx], nums[min_idx]
        a, b = b, a
        drawData(nums, [DARK_YELLOW if x == min_idx or x == idx else DARK_GREEN for x in range(len(nums))] )
        time.sleep(timee)
    drawData(nums, [DARK_GREEN for x in range(len(nums))])

