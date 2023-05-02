import linkedlist


def enqueue(Q, element):
    linkedlist.add(Q, element)
    return


def dequeue(Q):
  currentNode = Q.head
  previousNode = currentNode
  
  if (currentNode == None):
    return
    
  while (currentNode.nextNode != None):
    previousNode = currentNode
    currentNode = currentNode.nextNode

  if (previousNode == currentNode):
    valor = currentNode.value
    Q.head = None
    return valor
  else:
    valor = previousNode.nextNode.value
    previousNode.nextNode = None
    return valor
  
def firstEntrance(Q):
  currentNode = Q.head
  if currentNode == None:
    return
  while currentNode != None:
    if currentNode.nextNode == None:
      return currentNode
    currentNode = currentNode.nextNode
  
