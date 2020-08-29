###########quick sort#############
class Quick:
    def __init__(self, arr):
        self.arr = arr

    def partition(self, arr, low, high):
        pivot = arr[high]
        smaller_element_idx = low -1


        for j in range(low, high):
            if arr[j] < pivot:
                smaller_element_idx += 1
                arr[smaller_element_idx], arr[j] = arr[j], arr[smaller_element_idx]

        arr[smaller_element_idx+1], arr[high] = arr[high], arr[smaller_element_idx+1]
        return (smaller_element_idx+1)


    def quicksort(self, arr, low, high):
        if low < high:
            part = self.partition(arr, low, high)


            self.quicksort(arr, low, part-1)
            self.quicksort(arr, part+1, high)


    def print_array(self,arr):
        self.arr =arr
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
