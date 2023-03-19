import linkedlist

L = linkedlist.LinkedList

linkedlist.add(L, 4)
linkedlist.add(L, 3)
linkedlist.add(L, 2)
linkedlist.add(L, 7)
linkedlist.add(L, 9)
linkedlist.add(L, 1)
linkedlist.add(L, 8)

linkedlist.printLinkedList(L)

print("")

linkedlist.halfSort(L)

linkedlist.printLinkedList(L)