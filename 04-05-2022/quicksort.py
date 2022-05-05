def QuickSort(arr):
  length = len(arr)
  
  #Base case
  if length < 2:
      return arr

  #Position of the partitioning element
  position = 0 

  #Partitioning loop
  for i in range(1, length): 
        if arr[i] <= arr[0]:
            position += 1
            temp = arr[i]
            arr[i] = arr[position]
            arr[position] = temp

  temp = arr[0]
  arr[0] = arr[position] 
  #Brings pivot to it's appropriate position

  arr[position] = temp 
  #Sorts the length to the left of pivot

  left = QuickSort(arr[0:position]) 
  #sorts the length to the right of pivot

  right = QuickSort(arr[position+1:length])
  #Merging everything together
  
  arr = left + [arr[position]] + right 
  
  return arr

a = [9,8,7,6,4,5]
print(QuickSort(a))