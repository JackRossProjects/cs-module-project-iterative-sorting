def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # helper function takes same array and target but also takes L and R pointers
    return binarySearchHelper(arr, target, 0, len(arr) - 1)


def binarySearchHelper(arr, target, left, right):
    # check base case: out of order array
    if left > right:
        return -1  # not found
    # middle pointer = (left pointer + right) pointer divided by 2, rounded down
    middle = (left + right) // 2
    # check if middle pointers value is a match
    potential_match = arr[middle]
    if target == potential_match:
        return middle
    # if target is less than potential match, use values on the left of middle
    elif target < potential_match:
        return binarySearchHelper(arr, target, left, middle - 1)
    # else, use values on right of middle
    else:
        return binarySearchHelper(arr, target, middle + 1, right)