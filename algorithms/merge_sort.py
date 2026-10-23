# Break the array in half continually: 7 = 3 + 4 -> 3 = 1 + 2 -> sort (2) first then merge with (1)
def merge_sort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    
    mid = size // 2
    left = arr[:mid]
    right = arr[mid:]
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = [] # an array that stores the sorted array
    i = j = 0 # start from the first element
    
    # end at the last element until there is nothing to compare with
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 # iterate to the next element
        else:
            result.append(right[j])
            j += 1 # iterate to the next element
    
    # The while loop ends, that means there is nothing left to compare.
    # e.g.: the left array is done comparing, leaving the right array.
    # But the right array is sorted internally, so you could just combine result and the right array
    # Either left or right array is empty
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result            
    
def main():
    numbers = [7,5,9,3,5,4,8,10]
    sorted = merge_sort(numbers)
    print(sorted)
    
if __name__ == "__main__":
    main()