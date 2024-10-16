def birthdayCakeCandles(candles):
    counter = 0 #if largest candels have multiple alike candles it will get +1
    maximum = 0  # just the max height of candle
    n = len(candles)
    
    for i in range(n):
        if candles[i] > maximum:
            maximum = candles[i]
            counter = 1
        elif candles[i] == maximum:
            counter += 1
        else:
            continue
     
    return counter
