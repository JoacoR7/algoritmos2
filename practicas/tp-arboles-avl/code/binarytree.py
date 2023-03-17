import linkedlist
import myqueue


class BinaryTree:
    root = None


class BinaryTreeNode:
    key = None
    value = None
    leftnode = None
    rightnode = None
    parent = None


def search(B, element):
    return searchRecursivo(B.root, element)


def searchRecursivo(node, element):
    if (node == None):
        return None

    if (node.value == element):
        return node.key

    leftNode = searchRecursivo(node.leftnode, element)
    if (leftNode != None):
        return leftNode

    rightNode = searchRecursivo(node.rightnode, element)
    if (rightNode != None):
        return rightNode


def insertRecursivo(newNode, currentNode):
    if (currentNode.key > newNode.key):
        if (currentNode.leftnode == None):
            currentNode.leftnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else:
            insertRecursivo(newNode, currentNode.leftnode)
    elif (currentNode.key < newNode.key):
        if (currentNode.rightnode == None):
            currentNode.rightnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else:
            insertRecursivo(newNode, currentNode.rightnode)

    else:
        return None


def insert(B, element, key):
    newNode = BinaryTreeNode()
    newNode.key = key
    newNode.value = element

    if (B.root == None):
        B.root = newNode
        return key
    return insertRecursivo(newNode, B.root)


def delete(B, element):
    key = search(B, element)
    if (key == None):
        return None
    else:
        node = searchRecursivoKey(B.root, key)
        return deleteCasos(B, node)


def deleteKey(B, key):
    key = searchRecursivoKey(B.root, key)
    if (key == None):
        return None
    else:
        node = searchRecursivoKey(key)
        return deleteCasos(B, node)


def searchKey(B, key):
    return searchRecursivoKey(B.root, key)


def searchRecursivoKey(node, key):
    if (node == None):
        return None
    if (node.key == key):
        return node
    rightNode = searchRecursivoKey(node.rightnode, key)
    if (rightNode != None):
        return rightNode
    leftNode = searchRecursivoKey(node.leftnode, key)
    if (leftNode != None):
        return leftNode


#Divido en casos para orientar mejor el código:
#Caso 1: el nodo a eliminar es una hoja
#Caso 2: el nodo a eliminar tiene un hijo del lado izquierdo
#Caso 3: el nodo a eliminar tiene un hijo en el lado derecho
#Caso 4: el nodo a eliminar tiene dos hijos


def deleteCasos(B, node):
    if (node == None):
        return node

    #Caso 1
    if (node.leftnode == None and node.rightnode == None):

        if (node.parent.leftnode != None and node.parent.leftnode == node):
            node.parent.leftnode = None

        if (node.parent.rightnode != None and node.parent.rightnode == node):
            node.parent.rightnode = None

    #Caso 2
    elif (node.leftnode != None and node.rightnode == None):
        if (node.parent.leftnode != None and node.parent.leftnode == node):
            node.parent.leftnode = node.leftnode
        if (node.parent.rightnode != None and node.parent.rightnode == node):
            node.parent.rightnode = node.leftnode
    #Caso 3
    elif (node.leftnode == None and node.rightnode != None):
        if (node.parent.leftnode != None and node.parent.leftnode == node):
            node.parent.leftnode = node.rightnode
        if (node.parent.rightnode != None and node.parent.rightnode == node):
            node.parent.rightnode = node.rightnode
    #Caso 4
    #Tengo dos opciones: elegir el mayor de los nodos de la rama izquierda, o el menor de la rama derecha
    #Creo dos funciones para poder buscar estos nodos
    else:
        
		# biggestnode = biggestNode(node.leftnode)
		# biggestnode.parent = None
		# if(node.leftnode == biggestnode):
		# 	node.leftnode = None
		# if(node.rightnode == biggestnode):
		# 	node.rightnode = None
		# biggestnode.leftnode = node.leftnode
		# biggestnode.rightnode = node.rightnode
		# if(biggestnode.rightnode != None):
		# 	biggestnode.rightnode.parent = biggestnode
		# if(biggestnode.leftnode != None):
		# 	biggestnode.leftnode.parent = biggestnode
		# B.root = biggestnode


        smallestnode = smallestNode(node.rightnode)

        smallestnode.parent = None
        if (node.leftnode == smallestnode):
            node.leftnode = None
        if (node.rightnode == smallestnode):
            node.rightnode = None
        smallestnode.leftnode = node.leftnode
        smallestnode.rightnode = node.rightnode
        if (smallestnode.rightnode != None):
            smallestnode.rightnode.parent = smallestnode
        if (smallestnode.leftnode != None):
            smallestnode.leftnode.parent = smallestnode
        B.root = smallestnode

    return node.key


def biggestNode(node):
    if (node.rightnode != None):
        currentNode = biggestNode(node.rightnode)
        if (currentNode != None):
            return currentNode
    else:
        return node


def smallestNode(node):
    if (node.leftnode != None):
        currentNode = smallestNode(node.leftnode)
        if (currentNode != None):
            return currentNode

    else:
        return node


def accessRecursivo(node, key):
    if (node == None):
        return None
    if (node.key < key):
        return accessRecursivo(node.rightnode, key)
    elif (node.key > key):
        return accessRecursivo(node.leftnode, key)
    else:
        return node.value


def access(B, key):
    return accessRecursivo(B.root, key)


def update(B, element, key):
    node = searchRecursivoKey(B.root, key)
    if (node == None):
        return
    else:
        node.value = element
        return node.key


def traverseInOrder(B):
    L = linkedlist.LinkedList()
    traverseInOrderRecursivo(L, B.root)
    return L


def traverseInOrderRecursivo(L, node):
    if (node != None):
        traverseInOrderRecursivo(L, node.leftnode)
        linkedlist.add(L, node.value)
        traverseInOrderRecursivo(L, node.rightnode)
			
def traverseInOrderRecursivoKeys(L, node):
    if (node != None):
        traverseInOrderRecursivoKeys(L, node.leftnode)
        linkedlist.add(L, node.key)
        traverseInOrderRecursivoKeys(L, node.rightnode)

def traverseInPostOrder(B):
    L = linkedlist.LinkedList()
    traverseInPostOrderRecursivo(L, B.root)
    return L


def traverseInPostOrderRecursivo(L, node):
    if (node != None):
        traverseInPostOrderRecursivo(L, node.leftnode)
        traverseInPostOrderRecursivo(L, node.rightnode)
        linkedlist.add(L, node.value)
			
def traverseInPostOrderRecursivoKeys(L, node):
    if (node != None):
        traverseInPostOrderRecursivoKeys(L, node.leftnode)
        traverseInPostOrderRecursivoKeys(L, node.rightnode)
        linkedlist.add(L, node.value)

def traverseInPreOrder(B):
    L = linkedlist.LinkedList()
    traverseInPreOrderRecursivo(L, B.root)
    return linkedlist.revertList(L)


def traverseInPreOrderRecursivo(L, node):
    if (node != None):
        linkedlist.add(L, node.value)
        traverseInPreOrderRecursivo(L, node.leftnode)
        traverseInPreOrderRecursivo(L, node.rightnode)


def traverseInPreOrderKeys(B):
    L = linkedlist.LinkedList()
    traverseInPreOrderRecursivo(L, B.root)
    return linkedlist.revertList(L)


def traverseInPreOrderRecursivoKeys(L, node):
    if (node != None):
        linkedlist.add(L, node.value)
        traverseInPreOrderRecursivoKeys(L, node.leftnode)
        traverseInPreOrderRecursivoKeys(L, node.rightnode)


def traverseBreadFirst(B):

    if (B.root == None):
        return None

    nodesQueue = linkedlist.LinkedList()
    valuesQueue = linkedlist.LinkedList()
    myqueue.enqueue(nodesQueue, B.root)

    while (nodesQueue.head != None):
        node = myqueue.dequeue(nodesQueue)
        myqueue.enqueue(valuesQueue, node.value)
        if (node.leftnode != None):
            myqueue.enqueue(nodesQueue, node.leftnode)
        if (node.rightnode != None):
            myqueue.enqueue(nodesQueue, node.rightnode)
    valuesQueue = linkedlist.revertList(valuesQueue)
    return valuesQueue


def height(B):
    if (B.root == None):
        return 0
    return heightRecursivo(B.root)


def max(a, b):
    if (a >= b):
        return a
    return b


def heightRecursivo(node):
    if (node == None):
        return 0
    leftHeight = heightRecursivo(node.leftnode)
    rightHeight = heightRecursivo(node.rightnode)
    return max(leftHeight, rightHeight) + 1


def isBalanced(B):
    if (B.root == None):
        return False
    else:
        leftHeight = heightRecursivo(B.root.leftnode)
        rightHeight = heightRecursivo(B.root.rightnode)
        if (leftHeight == rightHeight or leftHeight == rightHeight + 1
                or leftHeight == rightHeight - 1):
            return True
        return False


def isSubTree(B1, B2):
    if (height(B1) <= height(B2)):
        return False
    if (B1 == None):
        return False
    if (B2 == None):
        return True
    return subTreeRecursivo(B1.root, B2.root, 0)


def subTreeRecursivo(node1, node2, check):

    if (node1.key == node2.key and node1.value == node2.value):
        check = 1
        if (node1.leftnode != None and node2.leftnode != None):
            return subTreeRecursivo(node1.leftnode, node2.leftnode, check)
        if (node1.rightnode != None and node2.rightnode != None):
            return subTreeRecursivo(node1.rightnode, node2.rightnode, check)
    if (node1.key != node2.key or node1.value != node2.value):
        if (check == 1):
            return False
        if (node1.leftnode != None):
            return subTreeRecursivo(node1.leftnode, node2, check)
        if (node1.rightnode != None):
            return subTreeRecursivo(node1.rightnode, node2, check)
        return False
    return True


def checkBST(B):
    if (B.root == None):
        return False
    return isBST(B.root)


def isBST(node):
    if (node.leftnode != None):
        if (node.key <= node.leftnode.key):
            return False
        isBST(node.leftnode)
    if (node.rightnode != None):
        if (node.key >= node.rightnode.key):
            return False
        isBST(node.rightnode)
    return True
