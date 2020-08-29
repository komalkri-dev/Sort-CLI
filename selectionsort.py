########selection sort#############
class Selection:
    def __init__(self, arr):
        self.arr = arr
        
    def selectionsort(self,arr):
        self.arr= arr
        if len(arr) > 1:
            for i in range(len(arr)):
                min_index = i

                for j in range(i+1, len(arr)):
                    if arr[min_index] > arr[j]:
                        min_index = j

                arr[i], arr[min_index] = arr[min_index], arr[i]


    def print_array(self,arr):
        self.arr = arr
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
