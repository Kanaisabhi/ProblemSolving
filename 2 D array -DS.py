def hourglassSum(arr):
    maxsum = -99
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bot = sum(arr[i+2][j:j+3])
            
            hourglass = top + mid + bot
            maxsum = max(maxsum,hourglass)
    return maxsum
    
