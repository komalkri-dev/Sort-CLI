class Bubble:
    def __init__(self, arr):
        self.arr = arr

    def bubble_sort(self,list):
        for iter_num in range(len(list)-1, 0, -1):
            for indx in range(iter_num):
                if list[indx]>list[indx+1]:
                    temp=list[indx]
                    list[indx]=list[indx+1]
                    list[indx+1]=temp

    def print_array(self,arr):
        self.arr = arr
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()


    