# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end < start:
        return -1

    mid = (start + end) // 2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start=start, end=mid-1)
    else:
        return binary_search(arr, target, start=mid+1, end=end)


def desc_binary_search(arr, target, start, end):
    # This honestly doesn't work I just copy pasted it oops
    if end < start:
        return -1

    mid = (start + end) // 2

    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return desc_binary_search(arr, target, start=start, end=mid-1)
    else:
        return desc_binary_search(arr, target, start=mid+1, end=end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively

def agnostic_binary_search(arr, target):
    if arr[0] > arr[1]:
        is_ascending = False
    else:
        is_ascending = True
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    else:
        return desc_binary_search(arr, target, 0, len(arr) - 1)
