import time
from colors import *
import time
from colors import *

def counting_sort(data, drawData, timee):
    n = max(data) + 1
    count = [0] * n
    for item in data:
        count[item] += 1
    
    k = 0
    for i in range(n):
        for j in range(count[i]):
            data[k] = i 
            drawData(data, [DARK_ORANGE if x==k else DARK_YELLOW if x==i else DARK_GREEN for x in range(len(data))] )
            time.sleep(timee)
            k += 1

    drawData(data, [DARK_GREEN for x in range(len(data))])
    