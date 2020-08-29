#######merger sort ###############
class Merge:
    def __init__(self, arr):
        self.arr = arr

    def mergesort(self,arr):
        self.arr = arr
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

    def print_array(self,arr):
        self.arr = arr
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()
