import linkedlist


def push(S, element):
    linkedlist.add(S, element)
    return


def pop(S):
    currentNode = S.head
    if (currentNode == None):
        return
    else:
        S.head = currentNode.nextNode
        return currentNode.value

