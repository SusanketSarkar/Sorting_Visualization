from tkinter import *
from tkinter import ttk
import random
from colors import *
from pyparsing import White


# Import the algorithms stored in the Algorithms folder
from Algorithms.bubbleSort import bubble_sort
from Algorithms.selectionSort import selection_sort
from Algorithms.insertionSort import insertion_sort
from Algorithms.mergeSort import merge_sort
from Algorithms.quickSort import quick_sort
from Algorithms.heapSort import heap_sort
from Algorithms.countingSort import counting_sort




window = Tk()
window.title("Visualize your Sorting Algorithmss")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Heap Sort', 'Counting Sort', 'Insertion Sort', 'Quick Sort', 'Selection Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# This function will generate the array
def generate():
    global data
    data = []
    text_from_box=t1.get(1.0, "end-1c")
    #print(text_from_box)
    if (text_from_box != ''):
        text=text_from_box.split(',')
        data=list(map(int,text))
    else: generate_random(data)
    drawData(data, [DARK_GREEN for x in range(len(data))])

# This function will generate a array if no input is given
def generate_random(data):
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)
    

# This function will set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.05
    else:
        return 0.001

# Function returns time complexity
def timecomp():
    if algo_menu.get() == 'Bubble Sort':
        return 'O(N*N)'
    elif algo_menu.get() == 'Selection Sort':
        return 'O(N*N)'
    elif algo_menu.get() == 'Insertion Sort':
        return 'O(N*N)'
    elif algo_menu.get() == 'Merge Sort':
        return 'O(Nlog(N))'
    elif algo_menu.get() == 'Quick Sort':
        return 'O(N*N)'
    elif algo_menu.get() == 'Heap Sort':
        return 'O(Nlog(N))'
    elif algo_menu.get() == 'Counting Sort':
        return 'O(N+k)'

# This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timee = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timee) 
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timee)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timee)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timee)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timee)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timee)
    elif algo_menu.get() == 'Counting Sort':
        counting_sort(data, drawData, timee)

### User interface here ###
UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm 
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed 
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# textbox to input an array
l3 = Label(UI_frame,  text="Input List: (optional)", bg=WHITE)
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
t1 = Text(UI_frame, height=1, width=20)
t1.grid(row=2, column=1, padx=5, pady=5)

# Shows the Time complexity 
l3 = Label(UI_frame,  text="Time Complexity: "+timecomp(), bg=WHITE)
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
t1 = Text(UI_frame, height=1, width=20)
t1.grid(row=2, column=1, padx=5, pady=5)
# Shows the Space Complexity
l3 = Label(UI_frame,  text="Input List: (optional)", bg=WHITE)
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
t1 = Text(UI_frame, height=1, width=20)
t1.grid(row=2, column=1, padx=5, pady=5)

# sort button 
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=3, column=1, padx=5, pady=5)

# button for generating array 
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=3, column=0, padx=5, pady=5)

# canvas to draw our array 
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()