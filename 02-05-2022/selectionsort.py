def selection_sort(arr):
  for i in range(len(arr)-1):
      # To find the minimum value of the unsorted segment
      # We first assume that the first element is the lowest
      min_index = i
      # We then use j to loop through the remaining elements
      for j in range(i+1, len(arr)-1):
          # Update the min_index if the element at j is lower than it
          if arr[j] < arr[min_index]:
              min_index = j
      # After finding the lowest item of the unsorted regions, swap with the first unsorted item
      arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr