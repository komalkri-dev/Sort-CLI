import argparse
import sys
from termcolor import colored
import pyfiglet


try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None

style = {
    'Welcome': '#fac731 bold',
    'To': '#4688f1 bold',
    'Sort-Cli': '#673ab7 bold'}

with open('data.txt', "r") as f:
    file = f.read().splitlines()

arr = [int(element) for element in file]


#######merger sort ###############
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1
            k += 1

        #check if any element is left

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

########selection sort#############

def selectionsort(arr):
    if len(arr) > 1:
        for i in range(len(arr)):
            min_index = i

            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

########insertion sort##############

def insertionsort(arr):
    for i in range(len(arr)):
        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

###########quick sort#############
def partition(arr, low, high):
    pivot = arr[high]
    smaller_element_idx = low -1


    for j in range(low, high):
        if arr[j] < pivot:
            smaller_element_idx += 1
            arr[smaller_element_idx], arr[j] = arr[j], arr[smaller_element_idx]

    arr[smaller_element_idx+1], arr[high] = arr[high], arr[smaller_element_idx+1]
    return (smaller_element_idx+1)


def quicksort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)


        quicksort(arr, low, part-1)
        quicksort(arr, part+1, high)



#####heap sort using heapq module ######

from heapq import heappush, heappop

def heap_sort(arr):
    heap = []
    for element in arr:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered


####heapsort######
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left <n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()


parser = argparse.ArgumentParser(
    description='Sort-CLI, sort a text file or some given data.', prog = 'Sort-Cli.py')

parser.add_argument(
    '-B', '--bubblesort', default =False, action='store_true', help="Sort by bubble sort algorithm")
parser.add_argument(
    '-I', '--insertionsort', default =False, action='store_true', help="Sort by Insertion sort algorithm")
parser.add_argument(
    '-S', '--selectionsort', default =False, action='store_true', help="Sort by Selection sort algorithm")
parser.add_argument(
    '-M', '--mergesort', default =False, action='store_true', help="Sort by merge sort algorithm")
parser.add_argument(
    '-Q', '--quicksort', default =False, action='store_true', help="Sort by quick sort algorithm")
parser.add_argument(
    '-He', '--heapsort', default =False, action='store_true', help="Sort by heap sort algorithm")


if __name__ == '__main__':
    print("\n")
    print(colored(pyfiglet.figlet_format("Sort-Cli"), 'blue'))
    print(colored('Welcome to', 'green'),colored('Sort-Cli', 'green', attrs=['bold']))
    print("\n")
    args = parser.parse_args()

    if not (args.bubblesort or args.insertionsort or args.selectionsort or args.mergesort or args.quicksort or args.heapsort):
        print(parser.parse_args(['-h']))

    if args.insertionsort:
        print(colored('Information:', "yellow"), "Sorting file by Insertion sort\n")
        print("Before sort:", end = "\n")
        print_array(arr)
        insertionsort(arr)
        print("After sorting:", end = "\n")
        print_array(arr)

    elif args.selectionsort:
        print(colored('Information:', "yellow"), "Sorting file by Selection Sort\n")
        print("Before sort:", end = "\n")
        print_array(arr)
        selectionsort(arr)
        print("After sorting:", end = "\n")
        print_array(arr)

    elif args.mergesort:
        print(colored('Information:', "yellow"), "Sorting file by Merge Sort\n")
        print("Before sort:", end = "\n")
        print_array(arr)
        mergesort(arr)
        print("After sorting:", end = "\n")
        print_array(arr)

    elif args.quicksort:
        print(colored('Information:', "yellow"), "Sorting file by Quick Sort\n")
        length = len(arr)
        print("Before sorting:", end = "\n")
        print_array(arr)
        print("After sorting:", end = "\n")
        quicksort(arr, 0, length-1)
        print_array(arr)

    elif args.heapsort:
        print(colored('Information:', "yellow"), "Sorting file by Heap Sort\n")
        print("Before sort:", end = "\n")
        print_array(arr)
        heapsort(arr)
        print("After sorting:", end = "\n")
        print_array(arr)

    else:
        print(parser.parse_args(['-h']))
        sys.exit(2)
