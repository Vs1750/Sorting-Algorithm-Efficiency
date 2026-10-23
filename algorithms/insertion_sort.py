def insertion_sort(arr):
    size = len(arr)
    
    # arrange elements before the key
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            # overwrite the key with the value before it
            # and repeat it for the elements to the left
            arr[j + 1] = arr[j]
            j -= 1
            
        # overwrite the value with the key
        # it is the minimum value that is larger than the key in the subarray
        arr[j + 1] = key
            
def main():
    numbers = [7,5,9,3,5,4,8,10]
    insertion_sort(numbers)
    print(numbers)
    
if __name__ == "__main__":
    main()