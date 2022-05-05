def merge(arr, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge
    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = arr[left_index:middle + 1]
    right_copy = arr[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each arr
    left_index = 0
    right_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_index < len(left_copy) and right_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_index] <= right_copy[right_index]:
            arr[sorted_index] = left_copy[left_index]
            left_index = left_index + 1
        # Opposite from above
        else:
            arr[sorted_index] = right_copy[right_index]
            right_index = right_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index += 1

    '''We ran out of elements either in left_copy or right_copy
    so we will go through the remaining elements and add them'''
    while left_index < len(left_copy):
        arr[sorted_index] = left_copy[left_index]
        left_index = left_index + 1
        sorted_index = sorted_index + 1

    while right_index < len(right_copy):
        arr[sorted_index] = right_copy[right_index]
        right_index = right_index + 1
        sorted_index = sorted_index + 1
    return arr

def merge_sort(arr, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(arr, left_index, middle)
    merge_sort(arr, middle + 1, right_index)
    merge(arr, left_index, right_index, middle)
  

a = [9,8,7,6,4,5]
print(merge_sort(a,0,len(a)-1))
print(a)