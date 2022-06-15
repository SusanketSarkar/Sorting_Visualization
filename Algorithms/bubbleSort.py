import time
from colors import *

def bubble_sort(nums, drawData, timee):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                drawData(nums, [DARK_YELLOW if x == i or x == i+1 else DARK_GREEN for x in range(len(nums))] )
                time.sleep(timee)
                # Set the flag to True so we'll loop again
                swapped = True
    drawData(nums, [DARK_GREEN for x in range(len(nums))])