import random
import myqueue
import math


class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


class Bheap:
    bheaplist = LinkedList()

    def __str__(self):
        str_list = ""
        currentNode = self.bheaplist.head.nextNode
        while (currentNode != None):
            str_list = str_list + str(currentNode.value) + " "
            currentNode = currentNode.nextNode
        return str_list

# ---------------------------------ADD-------------------------------------


def add(L, element):
    node = Node()
    node.value = element

    if L.head == None:
        L.head = node
    else:
        currentNode = L.head
        node.nextNode = currentNode
        L.head = node


# -------------------------------Search-----------------------------------
def search(L, element):
    currentNode = L.head
    position = 0
    while currentNode != None:
        if currentNode.value == element:
            return position
        position += 1
        currentNode = currentNode.nextNode
    return


# -------------------------------Insert-----------------------------------
def insert(L, element, position):
    currentNode = L.head
    if position > length(L) or position < 0:
        return None
    elif position == 0:
        add(L, element)
        L.head.nextNode = currentNode
        return 0

    else:
        for i in range(1, position + 1):
            if (i == position):
                node = Node()
                node.value = element
                node.nextNode = currentNode.nextNode
                currentNode.nextNode = node
                position = i
            currentNode = currentNode.nextNode
        return position


# -------------------------------Delete-----------------------------------


def delete(L, element):
    currentNode = L.head
    position = search(L, element)
    if position == None:
        return
    elif position == 0:
        L.head = currentNode.nextNode
        return 0
    else:
        for i in range(0, position - 1):
            currentNode = currentNode.nextNode
        currentNode.nextNode = currentNode.nextNode.nextNode
        return position


# -------------------------------Lenght-------------------------------
def length(L):
    currentNode = L.head
    size = 0
    while currentNode != None:
        size += 1
        currentNode = currentNode.nextNode
    return size


# -------------------------------Print-------------------------------
def printLinkedList(L):
    currentNode = L.head
    while currentNode != None:
        print(currentNode.value)
        currentNode = currentNode.nextNode


# -------------------------------Update-------------------------------


def update(L, element, position):
    currentNode = L.head
    if position >= 0 and position < length(L):
        for i in range(0, position):
            currentNode = currentNode.nextNode
        currentNode.value = element
        return position
    return


# -------------------------------Access-------------------------------
def access(L, position):
    currentNode = L.head
    if position >= 0 and position < length(L):
        for i in range(1, position + 1):
            currentNode = currentNode.nextNode
        return currentNode.value
    return


# -------------------------------Invert-------------------------------
def revertList(L):
    reversedList = LinkedList()
    longitud = length(L)
    currentNode = L.head
    for i in range(longitud, 0, -1):
        add(reversedList, currentNode.value)
        currentNode = currentNode.nextNode
    return reversedList


def searchPreviousNode(L, position):
    currentNode = L.head
    for i in range(0, position - 1):
        currentNode = currentNode.nextNode
    return currentNode


def move(L, position_orig, position_dest):
    if (position_orig == position_dest):
        return
    elif (position_orig == 0):

        node_orig = L.head

        L.head = L.head.nextNode
        previousNode_dest = searchPreviousNode(L, position_dest)

        node_orig.nextNode = previousNode_dest.nextNode
        previousNode_dest.nextNode = node_orig

    elif (position_dest == 0):
        previousNode_orig = searchPreviousNode(L, position_orig)
        node_orig = previousNode_orig.nextNode

        previousNode_orig.nextNode = previousNode_orig.nextNode.nextNode

        node_orig.nextNode = L.head
        L.head = node_orig

    else:
        previousNode_orig = searchPreviousNode(L, position_orig)
        node_orig = previousNode_orig.nextNode

        previousNode_orig.nextNode = previousNode_orig.nextNode.nextNode

        previousNode_dest = searchPreviousNode(L, position_dest)
        node_orig.nextNode = previousNode_dest.nextNode
        previousNode_dest.nextNode = node_orig




# -------------------------------Ordenamient básico-------------------------------


def bubbleSort(L):
    longitud = length(L)
    for i in range(0, longitud - 1):
        for j in range(0, longitud - 1):
            if (access(L, j) > access(L, j + 1)):
                currentValue = access(L, j)
                update(L, access(L, j + 1), j)
                update(L, currentValue, j + 1)
    return L


def selectionSort(L):
    longitud = length(L)
    for i in range(0, longitud - 1):
        smallestValue = access(L, i)
        for j in range(i, longitud - 1):
            if (smallestValue > access(L, j+1)):
                smallestValue = access(L, j+1)
                positionToChange = j + 1
        currentValue = access(L, i)
        update(L, smallestValue, i)
        update(L, currentValue, positionToChange)
    return L


def insertionSort(L):
    longitud = length(L)
    for i in range(0, longitud - 1):
        for j in range(i, longitud - 1):
            if (access(L, i) > access(L, j+1)):
                move(L, j+1, i)
    return L

# -------------------------------Ordenamient avanzado-------------------------------


def quickSort(L):
    Lfinal = LinkedList()
    Lfinal = quickSortRecursivo(L, Lfinal)

    L.head = None
    currentNode = Lfinal.head
    while (currentNode != None):
        add(L, currentNode.value)
        currentNode = currentNode.nextNode
    return L


def quickSortRecursivo(L, Lfinal):
    LMenor = LinkedList()
    LMayor = LinkedList()

    if (length(L) > 1):

        pivote = random.randint(0, length(L)-1)
        node = Node()
        node.value = access(L, pivote)
        LMayor.head = node
        currentNode = L.head

        while (currentNode != None):
            if (currentNode.value < node.value):
                add(LMenor, currentNode.value)
            elif (currentNode.value > node.value):
                add(LMayor, currentNode.value)
            currentNode = currentNode.nextNode

        quickSortRecursivo(LMenor, Lfinal)
        quickSortRecursivo(LMayor, Lfinal)

    elif (L.head != None):
        add(Lfinal, L.head.value)

    return Lfinal


def mergeSort(L):
    lista1 = LinkedList()
    lista2 = LinkedList()
    longitud = length(L)

    if (longitud > 1):
        for i in range(0, longitud):
            elemento = access(L, i)
            if (i < longitud // 2):
                add(lista1, elemento)
            else:
                add(lista2, elemento)
        mergeSort(lista1)
        mergeSort(lista2)

        L.head = None

        i = j = k = 0
        L.head = None

        while i < length(lista1) and j < length(lista2):
            if (access(lista1, i) < access(lista2, j)):
                insert(L, access(lista1, i), k)
                i += 1
            else:
                insert(L, access(lista2, j), k)
                j += 1
            k += 1

        while i < length(lista1):
            insert(L, access(lista1, i), k)
            i += 1
            k += 1

        while j < length(lista2):
            insert(L, access(lista2, j), k)
            j += 1
            k += 1


def shiftUp(Bheap, i):
    if (i != 1):
        node = i
        while (i // 2 > 0):
            k = 1 // 2
            p = access(Bheap.bheaplist, k)
            h = access(Bheap.bheaplist, i)
            if (p < h):
                update(Bheap.bheaplist, h, k)
                update(Bheap.bheaplist, p, i)
        shiftUp(Bheap, node-1)


def shiftDown(BHeap, i, currentSize):
    if (currentSize == None):
        currentSize = length(Bheap.bheaplist) - 1
    if (currentSize > 1):
        while (i * 2 <= currentSize):

            maxC = maxChild(Bheap, i, currentSize)

            p = access(Bheap.bheaplist, i)
            h = access(Bheap.bheaplist, maxC)

            if (h != None and p < h):
                update(Bheap.bheaplist, h, i)
                update(Bheap.bheaplist, p, maxC)

            i = maxC
            currentSize -= 1
            shiftDown(Bheap, i, currentSize)


def maxChild(Bheap, i, currentSize):
    if (i * 2 + 1 > currentSize):
        return (i*2)
    else:
        if (access(Bheap.bheaplist, i*2) > access(Bheap.bheaplist, i*2+1)):
            return i*2
        else:
            return i*2+1


def deleteMax(Bheap):
    if (length(Bheap.bheaplist) > 1):
        retval = access(Bheap.bheaplist, 1)
        value = myqueue.dequeue(Bheap.bheaplist)
        update(Bheap.bheaplist, value, 1)
        shiftDown(Bheap, 1)
        return retval


def insertBheap(Bheap, k):
    pos = length(Bheap.bheaplist)
    if (pos == 0):
        add(Bheap.bheaplist, 0)
        pos += 1
    insert(Bheap.bheaplist, k, pos)
    currentSize = length(Bheap.bheaplist) - 1
    shiftUp(Bheap, currentSize)


def heapify(Bheap, L):
    i = length(L) // 2
    Bheap.bheaplist.head = L.head
    add(Bheap.bheaplist, 0)
    while (i > 0):
        shiftDown(Bheap, i)
        i -= 1


def HeapSort(L):
    if (L.head != None):
        Bheap = Bheap()
        heapify(Bheap, L)
        L.head = None
        HeapSortRecursivo(Bheap, L, length(Bheap.bheaplist))


def HeapSortRecursivo(Bheap, L, size):
    k = deleteMax(Bheap)
    add(L, k)
    shiftDown(Bheap, 1)
    if (size > 2):
        HeapSortRecursivo(Bheap, L, size - 1)


def halfSort(L):
    size = length(L)
    currentNode = L.head
    midNode = L.head
    k = 1
    smallerNodes = 0
    midPosition = 0
    position = 0
    smallerNodeCount = 0
    
    while (k <= size/2):
        midNode = midNode.nextNode
        midPosition = k
        k += 1


    while (currentNode != None):
        if (currentNode.value < midNode.value):
            smallerNodes += 1
            if(position < midPosition):
                smallerNodeCount += 1
        currentNode = currentNode.nextNode
        position += 1

    currentMidNode = midNode.nextNode
    currentNode = L.head
    if(smallerNodeCount == math.trunc(smallerNodes/2)):
        return L
    else:
        while(currentMidNode != None and smallerNodeCount < math.trunc(smallerNodes/2)):
            if(currentMidNode.value < midNode.value):
                if(currentNode.value > currentMidNode.value):
                    aux = currentNode.value
                    currentNode.value = currentMidNode.value
                    currentMidNode.value = aux
                    currentNode = currentNode.nextNode
                    smallerNodeCount += 1
            currentMidNode = currentMidNode.nextNode
                
                
                


