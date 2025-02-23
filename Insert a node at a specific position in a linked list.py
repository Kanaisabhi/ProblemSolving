def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if head == None:
        head = node
    else:
        count = 1
        temp = head
        while temp.next != None and count < position:
            temp = temp.next
            count +=1
        node.next = temp.next
        temp.next = node
    return head
