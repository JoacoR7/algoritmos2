class AVLTree:
    root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

def search(A, element):
    return searchRecursivo(A.root, element)


def searchRecursivo(AVLNode, element):
    if (AVLNode == None):
        return None

    if (AVLNode.value == element):
        return AVLNode.key

    leftNode = searchRecursivo(AVLNode.leftnode, element)
    if (leftNode != None):
        return leftNode

    rightNode = searchRecursivo(AVLNode.rightnode, element)
    if (rightNode != None):
        return rightNode
    
def printInOrder(AVLNode):
    if AVLNode != None:
        printInOrder(AVLNode.leftnode)

        print(AVLNode.value)

        printInOrder(AVLNode.rightnode)

def rotateLeft(AVLTree, AVLNode):
    newRoot = AVLNode.rightnode
    AVLNode.rightnode = newRoot.leftnode
    if AVLNode.rightnode is not None:
        AVLNode.rightnode.parent = AVLNode
    newRoot.leftnode = AVLNode
    if AVLNode.parent is None:
        AVLTree.root = newRoot
    elif AVLNode.parent.leftnode == AVLNode:
        AVLNode.parent.leftnode = newRoot
    else:
        AVLNode.parent.rightnode = newRoot
    newRoot.parent = AVLNode.parent
    AVLNode.parent = newRoot
    return newRoot

def rotateRight(AVLTree, AVLNode):
    newRoot = AVLNode.leftnode
    AVLNode.leftnode = newRoot.rightnode
    if AVLNode.parent == None:
        AVLTree.root = newRoot
    elif AVLNode.parent.leftnode == AVLNode:
        AVLNode.parent.leftnode = newRoot
        newRoot.parent = AVLNode.parent
    else:
        AVLNode.parent.rightnode = newRoot
        newRoot.parent = AVLNode.parent
    
    newRoot.rightnode = AVLNode
    AVLNode.parent = newRoot
    return newRoot
    


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

def calculateBalance(AVLTree):
    calculateBalanceRecursivo(AVLTree.root)
    return AVLTree

def calculateBalanceRecursivo(AVLNode):
    if (AVLNode != None):
        calculateBalanceRecursivo(AVLNode.leftnode)

        if (AVLNode.leftnode != None and AVLNode.rightnode != None):
            AVLNode.bf = heightRecursivo(AVLNode.leftnode) - heightRecursivo(AVLNode.rightnode)
        elif(AVLNode.leftnode != None):
            AVLNode.bf = heightRecursivo(AVLNode.leftnode)
        elif(AVLNode.rightnode != None):
            AVLNode.bf = -heightRecursivo(AVLNode.rightnode)
        else:
            AVLNode.bf = 0

        calculateBalanceRecursivo(AVLNode.rightnode)

def reBalance(AVLTree):
    calculateBalance(AVLTree)
    reBalanceRecursivo(AVLTree.root, AVLTree.root)
    return AVLTree

def reBalanceRecursivo(AVLNode, root):
    if(AVLNode.leftnode != None):
        reBalanceRecursivo(AVLNode.leftnode, root)

    if(AVLNode.bf == 0):
        return AVLNode.key

    A = AVLTree

    if(AVLNode.bf < -1):
        if(AVLNode.rightnode != None):
            if AVLNode.rightnode.bf > 0:
                rotateRight(A, AVLNode.rightnode)
                rotateLeft(A, AVLNode)
                calculateBalanceRecursivo(root)

            else:
                rotateLeft(A, AVLNode)
                calculateBalanceRecursivo(root)
    elif(AVLNode.bf > 1):
        if(AVLNode.leftnode != None):
            if AVLNode.leftnode.bf < 0:
                rotateLeft(A, AVLNode.leftnode)
                rotateRight(A, AVLNode)
                calculateBalanceRecursivo(root)
            else:
                rotateRight(A, AVLNode)
                calculateBalanceRecursivo(root)
            

    if(AVLNode.rightnode != None):
        reBalanceRecursivo(AVLNode.rightnode, root)

def insert(AVLTree, element, key):
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element

    if (AVLTree.root == None):
        AVLTree.root = newNode
        return key
    insertRecursivo(newNode, AVLTree.root)
    reBalance(AVLTree)
    return AVLNode.key

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

def delete(B, element):
    key = search(B, element)
    if (key == None):
        return None
    else:
        node = searchRecursivoKey(B.root, key)
        deleteCasos(B, node)
        reBalance(B)
        return node.key


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

def joinAVLTreesAndKey(A, B, x):
    newNode = AVLNode
    newNode.key = x
    newNode.value = x
    alturaA = height(A)
    alturaB = height(B)
    if(alturaA == alturaB):
        C = AVLTree
        newNode.leftnode = A.root
        newNode.rightnode = B.root
        C.root = newNode
        return C
    elif(alturaA < alturaB):
        currentNode = B.root
        while(heightRecursivo(currentNode) != alturaA):
            currentNode = currentNode.leftnode
            if(heightRecursivo(currentNode) == alturaA):
                newNode.parent = currentNode.parent
                currentNode.parent = newNode
                newNode.leftnode = A.root
                newNode.rightnode = currentNode
                return B
    else:
        currentNode = A.root
        while(heightRecursivo(currentNode) != alturaB):
            currentNode = currentNode.rightnode
            if(heightRecursivo(currentNode) == alturaB):
                newNode.parent = currentNode.parent
                currentNode.parent = newNode
                newNode.rightnode = B.root
                newNode.leftnode = currentNode
                return B


                
        
