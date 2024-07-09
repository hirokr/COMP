def partition(arr, l, h):
  p = arr[h]
  i = l-1

  for j in range(l, h):
    if arr[j] < p:
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]

  return i + 1

def quickSort(arr, l, h):
  if l<h:
    pivot = partition(arr, l, h)
    quickSort(arr, l, pivot-1)
    quickSort(arr, pivot+1, h)


def merge(arr1, arr2):
  i,j = 0
  newArr = []

  while i< len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      newArr.append(arr1[i])
      i+=1
    else:
      newArr.append(arr2[j])
      j+=1
  
  newArr.extend(arr1[i::])
  newArr.extend(arr2[j::])

  return newArr

def mergeSort(arr):
  if len(arr)>1:
    mid = len(arr)//2

    left = mergeSort(arr[:mid:])
    right = mergeSort(arr[mid::])

    return merge(left, right)