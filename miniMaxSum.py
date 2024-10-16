def miniMaxSum(arr):
    arr.sort()
    min = sum(arr[:-1])
    max = sum(arr[1:])
    print(min,max)
