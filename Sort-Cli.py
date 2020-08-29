import argparse
import sys
from termcolor import colored
import pyfiglet
from insertionsort import InsertionSort
from mergesort import Merge
from bubblesort import Bubble
from selectionsort import Selection
from quicksort import Quick
from heapsort import Heap

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


with open('data.txt', "r") as f:
    file = f.read().splitlines()

arr = [int(element) for element in file]

parser = argparse.ArgumentParser(description='Sort-CLI, sort a text file or some given data.', prog = 'Sort-Cli.py')

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

    if args.bubblesort:
        print(colored('Information:', "yellow"), "Sorting file by Bubble sort\n")
        print("Before sort:", end = "\n")
        bubble = Bubble(arr)
        bubble.print_array(arr)
        bubble.bubble_sort(arr)
        print("After sorting:", end = "\n")
        bubble.print_array(arr)


    if args.insertionsort:
        print(colored('Information:', "yellow"), "Sorting file by Insertion sort\n")
        print("Before sort:", end = "\n")
        ins = InsertionSort(arr)
        ins.print_array(arr)
        ins.insertionsort(arr) 
        print("After sorting:", end = "\n")
        ins.print_array(arr)


    elif args.selectionsort:
        print(colored('Information:', "yellow"), "Sorting file by Selection Sort\n")
        print("Before sort:", end = "\n")
        selection = Selection(arr)
        selection.print_array(arr)
        selection.selectionsort(arr)
        print("After sorting:", end = "\n")
        selection.selectionsort(arr)

    elif args.mergesort:
        print(colored('Information:', "yellow"), "Sorting file by Merge Sort\n")
        print("Before sort:", end = "\n")
        merge = Merge(arr)
        merge.print_array(arr)
        merge.mergesort(arr)
        print("After sorting:", end = "\n")
        merge.mergesort(arr)

    elif args.quicksort:
        print(colored('Information:', "yellow"), "Sorting file by Quick Sort\n")
        length = len(arr)
        print("Before sorting:", end = "\n")
        quick = Quick(arr)
        quick.print_array(arr)
        print("After sorting:", end = "\n")
        quick.quicksort(arr, 0, length-1)
        quick.print_array(arr)

    elif args.heapsort:
        print(colored('Information:', "yellow"), "Sorting file by Heap Sort\n")
        print("Before sort:", end = "\n")
        heap = Heap(arr)
        heap.print_array(arr)
        heap.heapsort(arr)
        print("After sorting:", end = "\n")
        heap.print_array(arr)

    else:
        print(parser.parse_args(['-h']))
        sys.exit(2)


