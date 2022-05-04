arr_1 = [1,4,5,6,7,10,3,11,9]

"""this function will return the array in ascending oeder using Boubble sort"""
def boubblesor_asc(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr


"""this function will return the array in descending oeder using Boubble sort"""
def boubblesor_desc(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr