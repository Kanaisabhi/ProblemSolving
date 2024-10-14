def plusMinus(arr):
    n = len(arr)
    
    pos_counter = 0
    neg_counter = 0
    zero_counter = 0
    
    for num in arr:
        if num > 0:
            pos_counter += 1
        elif num < 0:
            neg_counter += 1
        else:
            zero_counter += 1
        
    print(f"{pos_counter / n:.6f}")
    print(f"{neg_counter / n:.6f}")
    print(f"{zero_counter / n:.6f}")
