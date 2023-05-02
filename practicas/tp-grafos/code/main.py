import graph
import linkedlist
import algo1
import dictionary

V = linkedlist.LinkedList()
A = linkedlist.LinkedList()


graph.createEdge(1, 2, A)
graph.createEdge(1, 3, A)
graph.createEdge(1, 4, A)
graph.createEdge(3, 2, A)
graph.createEdge(2, 6, A)
graph.createEdge(5, 6, A)
#graph.createEdge(3, 6, A)

graph.createVertex(V, 6)


G = graph.createGraph(V, A)

graph.printAdjacencyMatrix(G)

print(graph.existPath(G, 4, 5))

print(graph.isConnected(G))

V1 = linkedlist.LinkedList()
A1 = linkedlist.LinkedList()

graph.createVertex(V1, 3)
graph.createEdge(1, 2, A1)
graph.createEdge(1, 3, A1)
graph.createEdge(3, 2, A1)

G1 = graph.createGraph(V1, A1)

#graph.printAdjacencyMatrix(G1)

print(graph.isComplete(G1))

B = graph.convertToBFSTree(G, 1)


graph.printAdjacencyMatrix(B[1])

a, b = graph.convertTree(G)

linkedlist.printLinkedList(b)
graph.printAdjacencyMatrix(a)
print(graph.countConnections(G))

g = graph.convertToDFSTree(G, 1)
graph.printAdjacencyMatrix(g)
"""
A = linkedlist.LinkedList()

graph.createEdge(1, 2, A)
graph.createEdge(1, 3, A)
graph.createEdge(2, 3, A)
graph.createEdge(3, 4, A)
graph.createEdge(2, 4, A)
graph.createEdge(5, 6, A)
graph.createEdge(5, 4, A)

V2 = graph.createGraph(V, A)

print()

G40 = graph.convertToDFSTree(V2, 1)

graph.printAdjacencyMatrix(G40)
"""