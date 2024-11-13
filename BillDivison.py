def bonAppetit(bill, k, b):
    # bill = price 
    # k anna didn't eat 
    # b anna payed
    total = sum(bill)
    charge = (total - bill[k])//2
    if b == charge:
        print('Bon Appetit')
    else:
        print(b - charge)
