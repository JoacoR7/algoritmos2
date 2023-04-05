import trietree
import linkedlist

T = trietree.Trie()



trietree.Trie.insert(T, "Ala")
trietree.Trie.insert(T, "Alado")
trietree.Trie.insert(T, "Bicho")
trietree.Trie.insert(T, "Hoy")
trietree.Trie.insert(T, "Hola")
trietree.Trie.insert(T, "Holi")
trietree.Trie.insert(T, "Honda")
trietree.Trie.insert(T, "Holiwi")
trietree.Trie.insert(T, "Holiwa")
trietree.Trie.insert(T, "Holanda")
#trietree.Trie.insert(T, "Aloh")

trietree.Trie.printTree(T)

print("")

palabras = trietree.findWords(T, "Ho")

linkedlist.printLinkedList(palabras)

print("--")

w = trietree.searchPattern(T, "Ho", 4)

linkedlist.printLinkedList(w)

print("---")

w = trietree.findAllWords(T)

linkedlist.printLinkedList(w)

T2 = trietree.Trie()

trietree.Trie.insert(T2, "Ala")
trietree.Trie.insert(T2, "Alado")
trietree.Trie.insert(T2, "Bicho")
trietree.Trie.insert(T2, "Hoy")
trietree.Trie.insert(T2, "Hola")
trietree.Trie.insert(T2, "Holi")
trietree.Trie.insert(T2, "Honda")
trietree.Trie.insert(T2, "Holiwi")
trietree.Trie.insert(T2, "Holiwa")
trietree.Trie.insert(T2, "Holanda")

print(trietree.areEqual(T, T2))

T3 = trietree.Trie()

trietree.Trie.insert(T3, "Hoy")
trietree.Trie.insert(T3, "Yoah")
trietree.Trie.insert(T3, "Yoh")

print(trietree.findReverseWord(T3))