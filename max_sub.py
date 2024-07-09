def maxSub(arr):
  maxSubArray = float('-inf')
  curMax = 0
  for i in arr:
    curMax += i
    maxSubArray = max(curMax, maxSubArray)
    if curMax < 0:
      curMax = 0
  return maxSubArray

def maxSubPrint(arr):
  maxSubArray = float('-inf') # storing max sum till current position
  curMax = 0 #
  ans_start = -1
  ans_end =  -1

  for i in range(len(arr)):
    if curMax == 0:
      start = i
    curMax += arr[i]
    
    if curMax > maxSubArray :
      maxSubArray = curMax
      ans_start = start
      ans_end = i
      
    if curMax < 0:
      curMax = 0

  print(arr[ans_start: ans_end+1:])
  return maxSubArray


def subArrayK(arr, k):
  res = 0
  curSum = 0
  preSum = {0:1}

  for i in arr:
    curSum +=i
    diff = curSum - k

    res += preSum.get(diff, 0)

    preSum[curSum] = 1 + preSum.get(curSum, 0)
  
  return res

def SK(arr, sum):
  curSum = 0
  start = 0
  end = -1


  map = {}

  for i in range(len(arr)):
    curSum +=  arr[i]

    if curSum - sum ==0:
      start = 0
      end = i
      break
    
    if (curSum - sum) in map.keys() :
      start = map[curSum - sum] + 1
      end =  i
      break
    map[curSum] = i

  if end == -1:
    print('Not')
  else:
    print(arr[start:end+1:])
    

def LargestSK(arr, sum):
  curSum = 0
  start = 0
  end = -1
  largest = 0
  large_st = 0
  large_end = 0
  map = {}

  for i in range(len(arr)):
    curSum +=  arr[i]

    if curSum - sum ==0:
      start = 0
      end = i
      break
    
    if (curSum - sum) in map.keys() :
      start = map[curSum - sum] + 1
      end =  i
      if end - start + 1 > largest:
        largest = end - start + 1
        large_st = start
        large_end = end
    map[curSum] = i

  if end == -1:
    print('Not')
  else:
    print(arr[large_st:large_end+1:])
    


arr = [10, 15, -5, 15, -10, 5]
sum = 5

print(SK(arr, sum))

def minSub(arr):
  minSubArray = float('inf')
  curMin = 0
  

# print(maxSubPrint([-2,-3,4,-1,-2,1,5,-1]))
  