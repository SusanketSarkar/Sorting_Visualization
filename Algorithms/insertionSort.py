import time
from colors import *

def insertion_sort(nums, drawData, timee):
    for i in range(1, len(nums)):
        j = i-1
        nxt_element = nums[i]
        # Compare the current element with next one
        while (nums[j] > nxt_element) and (j >= 0):
            nums[j+1] = nums[j]
            j=j-1
        nums[j+1] = nxt_element
        drawData(nums, [DARK_YELLOW if x==i else DARK_ORANGE if x==j+1 else DARK_GREEN for x in range(len(nums))] )
        time.sleep(timee)
    drawData(nums, [DARK_GREEN for x in range(len(nums))])