########insertion sort##############

class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def insertionsort(self, arr):
        for i in range(len(arr)):
            key = arr[i]

            j = i-1

            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key


    def print_array( self, arr):
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
