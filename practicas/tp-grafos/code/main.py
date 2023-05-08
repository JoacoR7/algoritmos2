import graph
import linkedlist
import algo1
import dictionary

A = linkedlist.LinkedList()


graph.createEdge(1, 2, A)
graph.createEdge(1, 3, A)
graph.createEdge(1, 4, A)
graph.createEdge(3, 2, A)
graph.createEdge(2, 6, A)
graph.createEdge(5, 6, A)
#graph.createEdge(3, 4, A)


G = graph.createGraph(6, A)

graph.printAdjacencyMatrix(G)
"""
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


l = graph.bestRoad(G, 4, 5)
print("Lista")
linkedlist.printLinkedList(l)

"""

A = linkedlist.LinkedList()

graph.createWeightedEdge(A, 3, 1, 2)
graph.createWeightedEdge(A, 1, 1, 3)
graph.createWeightedEdge(A, 1, 3, 1)
graph.createWeightedEdge(A, 2, 1, 4)
graph.createWeightedEdge(A, 2, 3, 2)
graph.createWeightedEdge(A, 2, 2, 6)
graph.createWeightedEdge(A, 2, 6, 5)
graph.createWeightedEdge(A, 4, 4, 7)
#TODO: REVISAR ESTE CASO
graph.createWeightedEdge(A, 1, 3, 7)


G = graph.createWeightedGraph(7, A, "D")

graph.printAdjacencyMatrix(G)

"""a = graph.PRIM(G)

graph.printAdjacencyMatrix(a)

a = graph.KRUSKAL(G)

graph.printAdjacencyMatrix(a)"""

graph.shortestPath(G, 1, 5)