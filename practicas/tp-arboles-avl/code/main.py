import avltree

A = avltree.AVLTree

avltree.insert(A, 20, 20)
avltree.insert(A, 10, 10)
avltree.insert(A, 40, 40)
avltree.insert(A, 5, 5)
avltree.insert(A, 18, 18)
avltree.insert(A, 80, 80)
avltree.insert(A, 100, 100)

avltree.printInOrder(A.root)
print("Raiz")
print(A.root.key)
print("")












