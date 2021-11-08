def removeDuplicates(head):
    node = head

    if head == None:
        return None
    

    while (node.next):

        if (node.val == node.next.val):
            node.next = node.next.next
            node = node.next
             
        else:
            node = node.next

    return head

"""
def stringPartition(str):
    counter = 0
    strLen = 0
    letters = {}

    for i in str:
"""
