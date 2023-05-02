import algo1
import dictionary
import linkedlist
import myqueue
import mystack


def createGraph(V, A):
    G = dictionary.Dictionary(linkedlist.length(V))
    
    arista = A.head
    
    while arista != None:
        addEdge(arista.value, G)
        arista = arista.nextNode
    
    return G

def addEdge(edge, G):
    if edge[0] > len(G.slots) or edge[1] > len(G.slots):
        return None
    
    slot1 = G.slots[edge[0] - 1]
    slot2 = G.slots[edge[1] - 1]

    slot1Inserted = False
    slot2Inserted = False

    if(slot1 == None):
        G.slots[edge[0] - 1] = linkedlist.LinkedList()
        G.slots[edge[0] - 1].head = linkedlist.Node()
        G.slots[edge[0] - 1].head.value = edge[1]
        slot1Inserted = True
    
    if(slot2 == None):
        G.slots[edge[1] - 1] = linkedlist.LinkedList()
        G.slots[edge[1] - 1].head = linkedlist.Node()
        G.slots[edge[1] - 1].head.value = edge[0]
        slot2Inserted = True

    if(not slot1Inserted):
        addEdgeAux(edge[0], edge[1], G)
    if(not slot2Inserted):
        addEdgeAux(edge[1], edge[0], G)

    return

def addEdgeAux(a, b, G):
    currentNode = G.slots[a-1].head

    inserted = False
    position = 0


    while not inserted and currentNode != None:
            if(currentNode.value > b):
                linkedlist.insert(G.slots[a-1], b, position)
                inserted = True
            else:
                position += 1
                currentNode = currentNode.nextNode
                if currentNode == None:
                    linkedlist.insert(G.slots[a-1], b, position)

def createEdge(a1, a2, A):
    edge = algo1.Array(2)

    edge[0] = a1
    edge[1] = a2

    linkedlist.add(A, edge)

def createVertex(V, length):
    if V.head != None:
        return
    for i in range(0, length):
        linkedlist.add(V, i+1)

def existPath(G, v1, v2):
    visitedNodes = linkedlist.LinkedList()
    return existPathAux(G, v1, v2, visitedNodes)

def existPathAux(G, v1, v2, visitedNodes):
    if(v1 > len(G.slots) or v2 > len(G.slots)):
        return False
    
    if visitedNodes != None:
        if linkedlist.search(visitedNodes, v1) != None:
            return False

    
    found = findConnection(G, v1, v2)

    if found:
        return True

    linkedlist.add(visitedNodes, v1)

    node = G.slots[v1 - 1]
    node = node.head

    while node != None:
        found = existPathAux(G, node.value, v2, visitedNodes)
        if found:
            return True
        node = node.nextNode

    return False

def findConnection(G, v1, v2):
    node = G.slots[v1 - 1]

    if node == None:
        return False
    
    node = node.head

    while node != None:
        if(node.value == v2):
            return True
        node = node.nextNode

    return False

def isConnected(G):
    for i in range(2, len(G.slots)):
        if existPath(G, 1, i) == False:
            return False
        
    return True
            
        
        
def isComplete(G):
    length = len(G.slots)
    for i in range(0, length):
        adjacencyList = G.slots[i]
        if adjacencyList == None:
            return False
        if(linkedlist.length(adjacencyList) != length - 1):
            return False
    return True

def isTree(G):
    if not isConnected(G):
        return False

def convertToBFSTree(G, v):
    A = linkedlist.LinkedList()
    V = linkedlist.LinkedList()
    createVertex(V, len(G.slots))
    visitedNodes = linkedlist.LinkedList()
    linkedlist.add(visitedNodes, v)
    longitud = len(G.slots)
    newGraph = dictionary.Dictionary(longitud)
    #Inicializo todos los vértices
    for i in range(0, longitud):
        newGraph.slots[i] = linkedlist.LinkedList()
        #Padre
        linkedlist.add(newGraph.slots[i], None)
        #Distancia
        linkedlist.add(newGraph.slots[i], 0)
        #Color
        linkedlist.add(newGraph.slots[i], "White")
    queue = linkedlist.LinkedList()
    myqueue.enqueue(queue, v-1)
    currentNode = queue.head
    while currentNode != None:
        if(newGraph.slots[currentNode.value].head.value == "White"):
            father = currentNode.value
            newGraph.slots[father].head.value = "Grey"
            son = G.slots[father]
            if son != None:
                son = son.head
            myqueue.dequeue(queue)
            while son != None:
                if linkedlist.search(visitedNodes, son.value) == None:
                    createEdge(father + 1, son.value, A)
                    myqueue.enqueue(queue, son.value-1)
                    newGraph.slots[son.value - 1].head.nextNode.value = newGraph.slots[father].head.nextNode.value + 1
                    newGraph.slots[son.value - 1].head.nextNode.nextNode.value = currentNode.value
                    linkedlist.add(visitedNodes, son.value)
                son = son.nextNode
            newGraph.slots[father].head.value = "Black"
            currentNode = myqueue.firstEntrance(queue)
    adjacencyList = createGraph(V, A)
    return newGraph, adjacencyList

def convertTree(G):
    if not isConnected(G):
        return
    _, adjacencyList = convertToBFSTree(G, 1)
    edgesToBeDeleted = linkedlist.LinkedList()
    for i in range(len(G.slots)):
        node = G.slots[i].head
        while node != None:
            if(linkedlist.search(adjacencyList.slots[i], node.value) == None):
                createEdge(i + 1, node.value, edgesToBeDeleted)
            node = node.nextNode
    

    return adjacencyList, edgesToBeDeleted

def countConnections(G):
    connections = 0
    for i in range(len(G.slots)):
        node = G.slots[i]
        if node == None:
            continue
        node = node.head
        while node != None:
            connections += 1
            node = node.nextNode
    return connections/2

def convertToDFSTree(G, v):
    v = v - 1
    longitud = len(G.slots)
    newGraph = dictionary.Dictionary(longitud)
    for i in range(longitud):
        newGraph.slots[i] = linkedlist.LinkedList()
        #Padre
        linkedlist.add(newGraph.slots[i], None)
        #Distancia
        linkedlist.add(newGraph.slots[i], 0)
        #Color
        linkedlist.add(newGraph.slots[i], "White")
    visitedNodes = linkedlist.LinkedList()
    edges = linkedlist.LinkedList()
    vertex = linkedlist.LinkedList()
    createVertex(vertex, len(G.slots))
    DFSVisit(G, v, visitedNodes, edges, newGraph)
    A = createGraph(vertex, edges)
    return A
    
def DFSVisit(G, slot, visitedNodes, edges, newGraph):
    son = G.slots[slot]
    if son == None:
        return
    son = son.head
    linkedlist.add(visitedNodes, slot+1)
    while True:
        if(linkedlist.search(visitedNodes, son.value) != None):
            son = son.nextNode
        else:
            son = son.value 
            newGraph.slots[son -1].head.nextNode.nextNode.value = slot
            createEdge(slot+1, son, edges)
            break
        if son == None:
            return   
    
    contador = 0
    DFSVisit(G, son-1, visitedNodes, edges, newGraph)
    DFSVisit(G, newGraph.slots[son-1].head.nextNode.nextNode.value, visitedNodes, edges, newGraph)
    
def printAdjacencyMatrix(G):
    print("  ", end="")
    for i in range(0, len(G.slots)):
        print(i + 1, end=" ")
    print("  ")
    for i in range(0, len(G.slots)):
        print("---", end="")
    print("")
    for i in range(0, len(G.slots)):
        slot = G.slots[i]
        if slot != None:
            slot = slot.head
        cont = len(G.slots)
        columna = 1
        print(i + 1, end="|")
        while slot != None or cont != 0:
            if(slot != None):
                nodo = slot.value
                while columna < nodo:
                    print(0, end=" ")
                    columna += 1
                    cont -= 1
                print(1, end=" ")
                slot = slot.nextNode
                columna += 1
                cont -= 1
                continue
            else:
                print(0, end=" ")
            cont -= 1

        print("")
        




