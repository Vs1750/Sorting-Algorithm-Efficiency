def bubble_sort(arr):
    size = len(arr)
    
    for i in range(size - 1):
        swapped = False
        
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    numbers = [7,5,9,3,5,4,8,10]
    bubble_sort(numbers)
    print(numbers)
    
if __name__ == "__main__":
    main()