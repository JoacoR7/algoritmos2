import dictionary
import linkedlist

d = dictionary.Dictionary(9)
d2 = dictionary.Dictionary(5)


""""
dictionary.printDictionary(d)

dictionary.insert(d, 10, "Hola")
dictionary.insert(d, 1, "Hola")
dictionary.insert(d, 3, "Adios")
dictionary.insert(d, 0, "Wenas")

print("Print after insertion")

dictionary.printDictionary(d)

print(dictionary.search(d, 10))

dictionary.delete(d, 10)

dictionary.printDictionary(d)


L = linkedlist.LinkedList()

for i in range(0, 10):
    linkedlist.add(L, i)

linkedlist.add(L, 1)

print(dictionary.hasUniqueElements(L))
"""
d3 = dictionary.stringCompression("aAa")

print(ord("a") - 71)
print(ord("A") - 65)

print(d3)

print(dictionary.isPermutation("Hola", "aloh"))