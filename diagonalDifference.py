
def diagonalDifference(arr):
    principal = 0
    secondary = 0
    n = len(arr)
    for i in range(n):
       principal += arr[i][i]
       secondary +=  arr[i][n-i-1]
    
    result = principal-secondary
    
    return abs(result)
  
