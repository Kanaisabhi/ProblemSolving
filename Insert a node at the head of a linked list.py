def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    if llist != None:
        node.next = llist
    return node
