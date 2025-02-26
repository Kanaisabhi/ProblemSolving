    if position == 0:
        llist = llist.next
    else:
        temp = llist
        counter = 1
        while temp != None and counter < position:
            temp = temp.next
            counter += 1
        temp.next = temp.next.next
    return llist
