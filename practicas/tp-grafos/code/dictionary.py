import linkedlist
import array

#array(n, linkedlist())

class Dictionary:

    slots = None

    def __init__(self, length = 0):
        self.slots = [None for i in range(length)]



class DictionaryItem:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


#Método división
def hashFunction(k, m):
    return k % m

def insert(D, key, value):
    item = DictionaryItem(key, value)
    slot = hashFunction(key, len(D.slots))
    position = 0
    if(D.slots[slot] == None):
        D.slots[slot] = linkedlist.LinkedList()
        linkedlist.add(D.slots[slot], item)
    elif(D.slots[slot].head == None):
        D.slots[slot] = linkedlist.LinkedList()
        linkedlist.add(D.slots[slot], item)
    else:
        currentNode = D.slots[slot].head
        while currentNode != None:
            if(currentNode.value.key < key):
                position += 1
            elif(currentNode.value.key > key):
                linkedlist.insert(D.slots[slot], item, position)
                break
            if(currentNode.nextNode == None):
                linkedlist.insert(D.slots[slot], item, position)
                break
            currentNode = currentNode.nextNode     
    return D

def insertInOrderBFS(BFS, i, key, value):
    node = linkedlist.Node()
    node.value = value
    node.key = key
    if BFS.slots[i] == None:
        L = linkedlist.LinkedList()
        linkedlist.add(L, node)
        BFS.slots[i] = L
    else:
        linkedlist.add(BFS.slots[i], node)
    return BFS

def search(D, key):
    slot = hashFunction(key, len(D.slots))
    currentNode = D.slots[slot]
    if (currentNode == None):
        return None
    else:
        currentNode = currentNode.head
    while currentNode != None:
        if(currentNode.value.key == key):
            return currentNode.value.value
        currentNode = currentNode.nextNode
    return None

def delete(D, key):
    slot = hashFunction(key, len(D.slots))
    currentNode = D.slots[slot]
    if (currentNode == None):
        return None
    else:
        currentNode = currentNode.head
    while currentNode != None:
        if(currentNode.value.key == key):
            linkedlist.delete(D.slots[slot], currentNode.value)
        currentNode = currentNode.nextNode
    return

def printDictionary(D):
    for i in range(0, len(D.slots)):
        currentNode = D.slots[i]
        if currentNode != None:
            currentNode = currentNode.head
        else:
            print("null", end="")
        while currentNode != None:
            print(currentNode.value.key, " - ", currentNode.value.value, end=" | ")
            currentNode = currentNode.nextNode
        print("")
        print("-------------")


def hasUniqueElements(L):
    d = Dictionary(linkedlist.length(L))
    currentNode = L.head
    while currentNode != None:
        if(search(d, currentNode.value) != None):
            return False
        insert(d, currentNode.value, currentNode.value)
        currentNode = currentNode.nextNode
    return True

def postalCodeHashFunction(char, k, m):
    return ord(char * (k + 1)) % m

def stringCompression(str):
    d = Dictionary(26)
    for i, char in enumerate(str):
        if(char != char.upper()):
            key = ord(char) - 71
        else:
            key = ord(char) - 65
        if(search(d, key) == None):
            insert(d, key, 1)
        else:
            cantidad = search(d, key) + 1
            delete(d, key)
            insert(d, key, cantidad)
    return compressedString(d, str)

def compressedString(D, str):
    string = ""
    for i in range(0, len(D.slots)):
        currentNode = D.slots[i]
        if currentNode != None:
            currentNode = currentNode.head
        while currentNode != None:
            key = currentNode.value.key
            if(key >= 26):
                key = key + 71
            else:
                key = key + 65
            string = string + chr(key) + repr(currentNode.value.value)
            currentNode = currentNode.nextNode
    if(len(string)/2 == len(str)):
        return str
    return string

def isPermutation(s, p):
    if(len(s) != len(p)):
        return False
    
    for i in range(0, len(s)):
        if(s[i].upper() != p[len(p) - i - 1].upper()):
            return False
        
    return True

def isSubset(S, T):
    if(linkedlist.length(S) > linkedlist.length(T)):
        return False
    
    ds = Dictionary(linkedlist.length(S))
    dt = Dictionary(linkedlist.length(T))

    currentNodeT = T.head
    while currentNodeT != None:
        insert(dt, currentNodeT.value, currentNodeT. value)
        currentNodeT = currentNodeT.nextNode
    
    currentNodeS = currentNodeS.head

    while currentNodeS != None:
        if(search(dt, currentNodeS.value) == None):
            return False
        currentNodeS = currentNodeS.nextNode
    
    return True