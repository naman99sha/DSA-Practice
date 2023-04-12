class Graph():
    def __init__(self) -> None:
        self.noOfNodes = 0
        self.adjacentList = {}
    def addVertex(self,node):
        self.adjacentList[node] = []
        self.noOfNodes = self.noOfNodes + 1
    def addEdge(self,node1,node2):
        if self.adjacentList.get(node1) == None or self.adjacentList.get(node2) == None:
            return "Create these nodes first"
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return
    def showConnections(self):
        return self.adjacentList

graph = Graph()
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')
graph.addEdge('0','1')
graph.addEdge('0','2')
graph.addEdge('1','2')
graph.addEdge('1','3')
graph.addEdge('2','4')
graph.addEdge('3','4')
graph.addEdge('4','5')
graph.addEdge('5','6')
print(graph.showConnections())