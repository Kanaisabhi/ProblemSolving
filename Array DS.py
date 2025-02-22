def reverseArray(a):
  #method 1_
  return a[::-1]
  #method2_
  a.reverse()
  return a
  #method3_
  left = 0
  right = len(a)-1
  while(left < right):
    a[left],a[right] = a[right],a[left]
    left +=1
    right -= 1
  return a
