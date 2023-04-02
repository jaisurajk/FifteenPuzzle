# author: Jaisuraj Kaleeswaran
# date: March 17, 2023
# file: graph.py creates a graph implementation of fifteen puzzle 
# input: User inputted edges and vertexes
# output: Graph of Fifteen puzzle

class Vertex: #Vertex Class
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph: #Graph Class
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):  # add a vertex to the graph
        self.numVertices += 1
        v = Vertex(key)
        self.vertList[key] = v
        return v

    def getVertex(self, n):  # get a vertex from the graph
        for i in self.vertList.values():
            if n == i.id:
                return i

    def __contains__(self, n):
        return n in self.vertList.values()

    def addEdge(self, f, t, weight = 0):  # add an edge to the graph
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()  # return the vertices of the graph

    def __iter__(self):
        return iter(self.vertList.values())  # return the graph

    def breadth_first_search(self, s):
        q = [s]
        verts = [s]  # list of vertices
        while q:  # while the queue is not empty
            s = q.pop(0)
            for i in self.vertList.values():
                if i.id == s:  # if the vertex is the one we are looking for
                    for j in i.getConnections():
                        if j.id not in verts:
                            for k in [verts, q]:
                                k.append(j.id)
        return verts  # return the list of vertices

    def depth_first_search(self):
        # list of vertices
        verts = [] 
        self.DFS(0, verts)  # call the recursive function
        return verts  # return the list of vertices

    def DFS(self, vid, path):
        path.append(vid)
        # for each neighbor of the vertex
        for i in self.vertList[vid].getConnections():
            if i.id not in path:
                self.DFS(i.id, path)  # call the function recursively

#Driver code to test graph.py
if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 0)
    g.addEdge(5, 4)
    g.addEdge(5, 2)

    for v in g:
        print(v)

    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False

    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]

    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]