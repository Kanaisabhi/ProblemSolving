def matchingStrings(stringList, queries):
    result = []
    for i in queries:
        counter = 0
        for j in stringList:
            if i == j:
                counter += 1
            else:
                pass
            
        result.append(counter)
    return result 
