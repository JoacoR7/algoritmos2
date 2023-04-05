import linkedlist
import string


class Trie:
    root = None

    def __init__(self):
        self.root = TrieNode(None, None)

    def insert(self, word):
        currentNode = self.root
        for i, char in enumerate(word.upper()):
            #Árbol sin raíz (es decir, creamos un árbol desde 0)
            if self.root == None:
                self.root = TrieNode(None, None)
                childNode = TrieNode(self.root, char)
                linkedlist.add(self.root.children, childNode)
                currentNode = childNode
            #Rama sin hijos (creamos una nueva familia para el nodo)
            elif currentNode.children.head == None:
                childNode = TrieNode(currentNode, char)
                linkedlist.add(currentNode.children, childNode)
                currentNode = childNode
            #Rama con hijos (agregamos un hijo a la familia)
            else:
                isUnsorted = True
                position = 0
                childNodeAux = currentNode.children.head
                while isUnsorted:
                    if (childNodeAux == None):
                        childNode = TrieNode(currentNode, char)
                        linkedlist.insert(currentNode.children, childNode, position)
                        isUnsorted = False
                        currentNode = childNode
                    else:
                        if(char < childNodeAux.value.key):
                            childNode = TrieNode(currentNode, char)
                            linkedlist.insert(currentNode.children, childNode, position)
                            isUnsorted = False
                            currentNode = childNode
                        if(char == childNodeAux.value.key):
                            currentNode = childNodeAux.value
                            isUnsorted = False
                        if(char > childNodeAux.value.key):
                            position += 1
                            childNodeAux = childNodeAux.nextNode          
            if i == len(word) - 1:
                currentNode.isEndOfWord = True

    def search(self, word):
        currentNode = self.root
        if (currentNode == None):
            return None
        currentNode = currentNode.children.head
        charFoundCounter = 0  
        charFoundBool = False 
        for i, char in enumerate(word.upper()):
            if currentNode.value.key == char:
                charFoundCounter += 1;
                charFoundBool = True
            elif charFoundCounter != 0:
                charFoundCounter = 0
                charFoundBool = False 
            if(charFoundBool):
                currentNode = currentNode.value.children.head
            else:
                while(currentNode != None and not charFoundBool):
                    if(currentNode.value.key == char):
                        charFoundCounter += 1;
                        charFoundBool = True
                    else:
                        currentNode = currentNode.nextNode
                if(currentNode == None and charFoundBool == False):
                    return False
            if charFoundCounter == i + 1:
                return True

    def delete(self, word):
        currentNode = self.root
        currentNode = currentNode.children.head
        #Caso 1: árbol vacío
        if currentNode == None:
            return False
        fatherNode = searchInBrothers(currentNode, word[0])
        #Caso 2: la palabra no se encuentra en el árbol
        if fatherNode == None:
            return False
        
        currentNode = fatherNode
        wordsFound = 0
        for i, char in enumerate(word.upper()):
            currentNode = searchInBrothers(currentNode, char)
            if(currentNode == None):
                return False
            
        
            #Se encontró un nodo que es final de palabra (puede ser de la que se quiere eliminar u otra)
            if currentNode.value.isEndOfWord:
                wordsFound += 1
                if(i < len(word) - 1):
                    lastWordNode = currentNode
                    lastWord = word[0:i+1]
            #Llegamos al final de palabra
            if(i == len(word) - 1):
                #En el recorrido hasta la última letra, sólo se encontró una palabra
                if(wordsFound == 1 and currentNode.value.children.head == None):
                    currentNode = currentNode.value.parent
                    while(currentNode != None):
                        if(linkedlist.length(currentNode.children) == 1):
                            currentNode.children = None
                        else: 
                            linkedlist.delete(currentNode.children, searchInBrothers(currentNode.children.head, word[i].upper()).value)
                            return True
                        currentNode = currentNode.parent
                        i -= 1
                        
                        
                    if(currentNode.value.children.head == None):
                        fatherNode = None
                    else:
                        currentNode.value.isEndOfWord = False
                else:
                    currentNode.value.isEndOfWord = False
                    return True
            currentNode = currentNode.value.children.head
        return False

    def printTree(self):
        if (self.root == None):
            print("Empty tree")
        printChildren(self, self.root)


class TrieNode:
    parent = None
    children = linkedlist.LinkedList()
    key = None
    isEndOfWord = False

    def __init__(self, parent, key):
        self.parent = parent
        self.children = linkedlist.LinkedList()
        self.key = key
        self.isEndOfWord = False


def printChildren(TrieTree, TrieNode):
    currentNode = TrieNode.children.head
    while currentNode != None:
        if(currentNode != None):
            if(linkedlist.search(TrieTree.root.children, currentNode.value) != None):
                print("---")
        print(currentNode.value.key, end = "")
        if(currentNode.value.isEndOfWord and currentNode.value.children.head == None):
            print("")
        elif(currentNode.value.isEndOfWord):
            print("", end = " ")
        printChildren(TrieTree, currentNode.value)
        currentNode = currentNode.nextNode

def searchInBrothers(currentNode, char):
    while currentNode != None:
            if currentNode.value.key == char.upper():
                return currentNode
            currentNode = currentNode.nextNode
    return None

def deleteWord(currentNode, word):
    currentNode = currentNode.value.children.head
    if currentNode != None:
        deleteWord(currentNode, word)
    if(currentNode.value.children.head == None):
        parentNode = currentNode.value.parent
        if(linkedlist.length(parentNode.children) == 1):
            currentNode == None
        else:
            if(parentNode.children.head.value == currentNode):
                parentNode.children.head = currentNode.nextNode


    
def findWords(T, pattern):
    listaPalabras = linkedlist.LinkedList()
    currentNode = T.root.children.head
    palabra = ""
    for i, char in enumerate(pattern):
        currentNode = searchInBrothers(currentNode, char.upper())
        if currentNode != None:
            if(i == len(pattern)-1):
                if currentNode.value.key == char.upper():
                    break
            currentNode = currentNode.value.children.head
        else:
            return None
        
        
    findWordsRec(currentNode, listaPalabras, palabra)
    return listaPalabras
    
def findAllWords(T):
    listaPalabras = linkedlist.LinkedList()
    currentNode = T.root.children.head
    palabra = ""
    findAllWordsRecursive(currentNode, listaPalabras, palabra)
    return listaPalabras

def findAllWordsRecursive(currentNode, palabras, palabra):
    if(currentNode == None):
        return
    while currentNode != None:
        letra = currentNode.value.key
        palabra = palabra + letra
        if(currentNode.value.isEndOfWord):
            linkedlist.add(palabras, palabra)
        findAllWordsRecursive(currentNode.value.children.head, palabras, palabra)
        palabra = palabra[0:len(palabra)-1]
        currentNode = currentNode.nextNode

def findWordsRec(TrieNode, palabras, palabra):
    currentNode = TrieNode.value.children.head
    while currentNode != None:
        letra = currentNode.value.key
        palabra = palabra + letra
        if(currentNode.value.isEndOfWord):
            linkedlist.add(palabras, palabra)
        findWordsRec(currentNode, palabras, palabra)
        palabra = palabra[0:len(palabra)-1]
        currentNode = currentNode.nextNode
    
def searchPattern(T, pattern, length):
    words = findWords(T, pattern)
    currentNode = words.head
    wordsOfInterest = linkedlist.LinkedList()
    while currentNode != None:
        
        currentNode.value = pattern.upper() + currentNode.value
        k = 0
        for i in enumerate(currentNode.value):
            k += 1
        if(k == length):
            linkedlist.add(wordsOfInterest, currentNode.value)
        currentNode = currentNode.nextNode
    
    return wordsOfInterest
    

def areEqual(T1, T2):
    wordList1 = findAllWords(T1)
    wordList2 = findAllWords(T2)

    currentNode1 = wordList1.head
    currentNode2 = wordList2.head

    while currentNode1 != None and currentNode2 != None:
        if(currentNode1.value != currentNode2.value):
            return False
        currentNode1 = currentNode1.nextNode
        currentNode2 = currentNode2.nextNode

    return True

def findReverseWord(T):
    wordList = findAllWords(T)
    currentNode = wordList.head
    currentNodeAux = wordList.head.nextNode

    while currentNodeAux != None and currentNode != None:
        if(currentNode.value == currentNodeAux.value[::-1]):
            return True
        currentNodeAux = currentNodeAux.nextNode
        if(currentNodeAux == None):
            currentNode = currentNode.nextNode
            currentNodeAux = currentNode
    return False