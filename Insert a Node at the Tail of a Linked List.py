def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head == None:
        head = node
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = node
    return head
