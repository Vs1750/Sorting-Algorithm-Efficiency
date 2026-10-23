def selection_sort(arr):
    size = len(arr)
    
    # put the smallest element in front
    for i in range(size - 1): # No need to swap the last element as there is only one element
        
        # Assume the first element is the smallest value
        min_idx = i
        
        for j in range(i + 1, size): # Iterate from the next element to the last
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    numbers = [7,5,9,3,5,4,8,10]
    selection_sort(numbers)
    print(numbers)
    
if __name__ == "__main__":
    main()