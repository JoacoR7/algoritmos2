import algo1
import dictionary
import linkedlist
import myqueue
import math

#Normal graph

def createGraph(length, A, type = None):
    G = dictionary.Dictionary(length)
    
    arista = A.head
    
    while arista != None:
        addEdge(arista.value, G, type)
        arista = arista.nextNode
    
    return G

def addEdge(edge, G, type = None):
    if edge[0] > len(G.slots) or edge[1] > len(G.slots):
        return None
    
    slot1 = G.slots[edge[0] - 1]
    if type == None:
        slot2 = G.slots[edge[1] - 1]
        slot2Inserted = False

    slot1Inserted = False
    

    if(slot1 == None):
        G.slots[edge[0] - 1] = linkedlist.LinkedList()
        G.slots[edge[0] - 1].head = linkedlist.Node()
        G.slots[edge[0] - 1].head.value = edge[1]
        slot1Inserted = True
    if type == None:
        if(slot2 == None):
            G.slots[edge[1] - 1] = linkedlist.LinkedList()
            G.slots[edge[1] - 1].head = linkedlist.Node()
            G.slots[edge[1] - 1].head.value = edge[0]
            slot2Inserted = True

    if(not slot1Inserted):
        addEdgeAux(edge[0], edge[1], G)
    if type == None:
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

def createVertex(length):
    V = linkedlist.LinkedList()
    for i in range(0, length):
        linkedlist.add(V, i+1)

def existPath(G, v1, v2, type = None):
    visitedNodes = linkedlist.LinkedList()
    return existPathAux(G, v1, v2, visitedNodes, type)

def existPathAux(G, v1, v2, visitedNodes, type = None):
    if(v1 > len(G.slots) or v2 > len(G.slots)):
        return False
    
    if visitedNodes != None:
        if linkedlist.search(visitedNodes, v1) != None:
            return False

    
    found = findConnection(G, v1, v2, type)

    if found:
        return True

    linkedlist.add(visitedNodes, v1)

    node = G.slots[v1 - 1]
    if node != None:
        node = node.head

    while node != None:
        if type == None:
            found = existPathAux(G, node.value[1], v2, visitedNodes, type)
        else:
            found = existPathAux(G, node.value[1], v2, visitedNodes, type)
        if found:
            return True
        node = node.nextNode

    return False

def findConnection(G, v1, v2, type = None):
    node = G.slots[v1 - 1]

    if node == None:
        return False
    
    node = node.head
    while node != None:
        if type == None:
            if(node.value == v2):
                return True
        else:
            if(node.value[1] == v2):
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
    edges = linkedlist.LinkedList()
    for i in range(len(G.slots)):
        node = G.slots[i]
        if node != None:
            node = node.head
        while node != None:
            linkedlist.add(edges, node)
            node = node.nextNode
    l = linkedlist.length(edges)
    l = l/2 
    if len(G.slots) - 1 == l:
        return True
    else:
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

def bestRoad(G, v1, v2):
    if not existPath(G, v1, v2):
        return None
    newGraph, _ = convertToBFSTree(G, v1)
    son = v2 - 1
    vertexList = linkedlist.LinkedList()
    while True:
        father = newGraph.slots[son].head.nextNode.nextNode.value
        son = father
        if son == v1 - 1:
            return vertexList
        linkedlist.add(vertexList, father + 1)

def printAdjacencyMatrix(G):
    if(type(G.slots[0].head.value) == type(0)):
        tipo = None
    else:
        tipo = "W"
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
                if(tipo == "W"):
                    valor = nodo[1]
                else:
                    valor = nodo
                while columna < valor:
                    print(0, end=" ")
                    columna += 1
                    cont -= 1
                
                #TEMPORAL
                if(tipo == "W"):
                    print(nodo[0], end=" ")
                else:
                    print(1, end=" ")
                slot = slot.nextNode
                columna += 1
                cont -= 1
                continue
            else:
                print(0, end=" ")
            cont -= 1

        print("")

#Weighted graph

class weightedEdge:
    value = None
    vertex = None

def createWeightedGraph(length, A, type = None):
    G = dictionary.Dictionary(length)
    
    arista = A.head
    
    while arista != None:
        addWeightedEdge(arista, G, type)
        arista = arista.nextNode
    
    return G

def addWeightedEdge(edge, G, type = None):
    edge = edge.value
    if edge.vertex[0] > len(G.slots) or edge.vertex[1] > len(G.slots):
        return None
    
    slot1 = G.slots[edge.vertex[0] - 1]
    if type == None:
        slot2 = G.slots[edge.vertex[1] - 1]
        slot2Inserted = False

    slot1Inserted = False
    

    if(slot1 == None):
        G.slots[edge.vertex[0] - 1] = linkedlist.LinkedList()
        G.slots[edge.vertex[0] - 1].head = linkedlist.Node()
        G.slots[edge.vertex[0] - 1].head.value = algo1.Array(2)
        G.slots[edge.vertex[0] - 1].head.value[0] = edge.value
        G.slots[edge.vertex[0] - 1].head.value[1] = edge.vertex[1] 
        slot1Inserted = True
    if type == None:
        if(slot2 == None):
            G.slots[edge.vertex[1] - 1] = linkedlist.LinkedList()
            G.slots[edge.vertex[1] - 1].head = linkedlist.Node()
            G.slots[edge.vertex[1] - 1].head.value = algo1.Array(2)
            G.slots[edge.vertex[1] - 1].head.value[0] = edge.value
            G.slots[edge.vertex[1] - 1].head.value[1] = edge.vertex[0] 
            slot2Inserted = True

    if(not slot1Inserted):
        addWeightedEdgeAux(edge.vertex[0], edge.vertex[1], edge.value, G)
    if type == None:
        if(not slot2Inserted):
            addWeightedEdgeAux(edge.vertex[1], edge.vertex[0], edge.value, G)

    return

def addWeightedEdgeAux(a, b, w, G):
    currentNode = G.slots[a-1].head

    inserted = False
    position = 0

    edge = algo1.Array(2)
    edge[0] = w
    edge[1] = b

    while not inserted and currentNode != None:
            if(currentNode.value[1] > b):
                linkedlist.insert(G.slots[a-1], edge, position)
                inserted = True
            else:
                position += 1
                currentNode = currentNode.nextNode
                if currentNode == None:
                    linkedlist.insert(G.slots[a-1], edge, position)

def createWeightedEdge(A, w, a1, a2):
    edge = weightedEdge()
    vertex = algo1.Array(2)

    edge.value = w
    vertex[0] = a1
    vertex[1] = a2
    edge.vertex = vertex

    linkedlist.add(A, edge)

def PRIM(G):
    visitedNodes = linkedlist.LinkedList()
    nodesToVisit = linkedlist.LinkedList()
    lenght = len(G.slots)
    linkedlist.add(nodesToVisit, 0)
    linkedlist.add(visitedNodes, 0)
    
    newEdges = linkedlist.LinkedList()
    while linkedlist.length(newEdges) < lenght-1:
        node = nodesToVisit.head
        smallestValue = 1/math.tan(math.pi) * -1
        smallestNode = None
        while node != None:
            nodeAux = G.slots[node.value].head
            while nodeAux != None:
                if nodeAux.value[0] < smallestValue and linkedlist.search(visitedNodes, nodeAux.value[1] - 1) == None:
                    smallestNode = nodeAux.value
                    smallestValue = smallestNode[0]
                    father = node.value
                nodeAux = nodeAux.nextNode            
            node = node.nextNode

        print(smallestNode)
        print(father + 1)
        createWeightedEdge(newEdges, smallestNode[0], father + 1, smallestNode[1])
        linkedlist.add(visitedNodes, smallestNode[1] - 1)
        linkedlist.add(nodesToVisit, smallestNode[1] - 1)

        
    newGraph = createWeightedGraph(lenght, newEdges)
    return newGraph

def KRUSKAL(G):
    nodesToVisit = linkedlist.LinkedList()
    lenght = len(G.slots)
    for i in range(lenght):
        node = G.slots[i].head
        while node != None:
            edge = algo1.Array(3)
            edge[0] = node.value[0]
            edge[1] = i + 1
            edge[2] = node.value[1]
            if nodesToVisit.head == None:
                linkedlist.add(nodesToVisit, edge)
            else:
                position = 0
                nodeToVisit = nodesToVisit.head
                while True:
                    if edge[0] <= nodeToVisit.value[0]:
                        linkedlist.insert(nodesToVisit, edge, position)
                        break
                    else:
                        position += 1
                    nodeToVisit = nodeToVisit.nextNode
                    if nodeToVisit == None:
                        linkedlist.insert(nodesToVisit, edge, position)
                        break
            node = node.nextNode

    linkedlist.printLinkedList(nodesToVisit)
    newEdges = linkedlist.LinkedList()
    addedEdges = 0
    node = nodesToVisit.head
    while linkedlist.length(newEdges) < lenght-1:
        if newEdges.head == None:
            createWeightedEdge(newEdges, node.value[0], node.value[1], node.value[2])
            addedEdges = 1
        else:
            if not existPath(auxGraph, node.value[1], node.value[2], "W"):
                createWeightedEdge(newEdges, node.value[0], node.value[1], node.value[2])
                addedEdges += 1

        auxGraph = createWeightedGraph(lenght, newEdges)
        node = node.nextNode
        
    newGraph = createWeightedGraph(lenght, newEdges)
    return newGraph

def smallestEdge(E, visitedNodes = linkedlist.LinkedList()):
    node = E.head
    smallestValue = 1/math.tan(math.pi) * -1
    smallestNode = None
    while node != None:
        if node.value[0] < smallestValue and linkedlist.search(visitedNodes, node.value[1] - 1) == None:
            smallestNode = node.value
            smallestValue = smallestNode[0]
        node = node.nextNode

    return smallestNode


#Directed graph

def graphMatrix(V, A):
    matriz = algo1.Array(len(V),)

def shortestPath(G, start, end):
    start -= 1
    end -= 1
    # Inicializar el registro de los costos mínimos a cada nodo como infinito
    distances = [float('inf')] * len(G.slots)
    # El costo mínimo para llegar al nodo de inicio es 0
    distances[start] = 0
    # Inicializar el registro de los nodos previos en el camino más corto
    previous = [None] * len(G.slots)
    # Inicializar la lista de nodos visitados
    visited = set()
    # Inicializar la lista de nodos no visitados
    unvisited = set(range(len(G.slots)))

    while unvisited:
        # Encontrar el nodo no visitado con el costo mínimo actual
        current = min(unvisited, key=lambda node: distances[node])
        # Marcar el nodo como visitado
        visited.add(current)
        unvisited.remove(current)
        if(G.slots[current] == None):
            continue
        # Actualizar los costos mínimos para los nodos vecinos no visitados
        for i in range(linkedlist.length(G.slots[current])):
            if i == 0:
                node = G.slots[current].head
            distance = node.value[0]
            neighbor = node.value[1] - 1
            if distance > 0 and neighbor not in visited:
                new_distance = distances[current] + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    # Actualizar el nodo previo en el camino más corto
                    previous[neighbor] = current
            node = node.nextNode
            if node == None:
                break

    # Construir el camino más corto desde el nodo de inicio hasta el nodo destino
    path = []
    current = end
    while True:
        path.append(current)
        current = previous[current]
        if current == None:
            break
    path.reverse()

    # Retornar la lista de nodos en el camino más corto o None si no hay camino
    return path if distances[end] < float('inf') else None