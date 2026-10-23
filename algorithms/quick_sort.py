# Quick sort finds the correct position of the pivot
# then sorts the elements to the left and right of the pivot

from random import randint

def partition(arr, low, high):
    pivot = arr[high]
    
    # i indicates the correct position of pivot found so far
    i = low - 1
    
    for j in range(low, high):
        
        # if the element is less than the pivot, increment i by 1 and 
        if arr[j] < pivot:
            
            # so that i is at the position of the element that is greater than the pivot
            # to be swapped with arr[j] which is less than the pivot
            i += 1
            swap(arr, i, j)
            
    # swap the pivot with the next element after the element that is less than the pivot
    # e.g. 2 4 5 7 1  10  13 15 9
    #                i + 1    pivot
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
def quick_sort(arr, low, high):
    if low < high: # if low == high, that means the array is empty
        swap(arr, randint(low, high), high)
        
        #pi is the index of the pivot
        pi = partition(arr, low, high)
        
        quick_sort(arr, low, pi - 1) # sort the elements to the left of the pivot
        quick_sort(arr, pi + 1, high) # sort the elements to the right of the pivot
            
def main():
    numbers = [7,5,9,3,5,4,8,10]
    size = len(numbers)
    
    quick_sort(numbers, 0, size - 1)
    print(numbers)
    
if __name__ == "__main__":
    main()