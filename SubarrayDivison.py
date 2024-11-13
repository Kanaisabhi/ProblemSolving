def birthday(s, d, m):
    # s contains no. of choclate pieces with number on it 
    # d is date {sum of choc. pieces must be "d"}
    # m is month {it is the number of allowed pieces to make sum 'd'}
    count = 0
    
    total = sum(s[:m])
    if total == d:
        count += 1
    for i in range(m,len(s)):
        total += s[i]
        total -= s[i-m]
        if total == d:
            count += 1 
    return count
    
