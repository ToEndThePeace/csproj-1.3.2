# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a_index = b_index = curIndex = 0
    # Your code here
    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            merged_arr[curIndex] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[curIndex] = arrB[b_index]
            b_index += 1
        curIndex += 1
    while a_index < len(arrA):
        merged_arr[curIndex] = arrA[a_index]
        a_index += 1
        curIndex += 1
    while b_index < len(arrB):
        merged_arr[curIndex] = arrB[b_index]
        b_index += 1
        curIndex += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2

        left = merge_sort(arr[:mid])   # recursively sort left side
        right = merge_sort(arr[mid:])  # recursively sort right side

        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
