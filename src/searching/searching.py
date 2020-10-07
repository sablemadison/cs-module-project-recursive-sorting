# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return 1
    midpoint = (start + end) // 2

    if target == arr[midpoint]:
        return midpoint
    
    else:
        if target < arr[midpoint]:

            end = midpoint - 1
        else: start = midpoint + 1
        
        
        return binary_search(arr, target, start, end)

    
    # starting point
    # ending point
    # target value. Check list of target value and if found return it
    # if not found, keep going,
    # base case = target found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here

