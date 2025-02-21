def rotateLeft(d, arr):
#method1--
     n = len(arr)
     temp = []
     for i in range(d,n):
         temp.append(arr[i])
     for j in range(0,d):
         temp.append(arr[j])
     arr = temp.copy()
     return arr

#method2--
    
    
    n = len(arr)
    arr[:]= arr[d:n]+arr[0:d]
    return arr
