#
# DO NOT FORGET TO ADD COMMENTS!!!
#
from collections import deque

class Vertex:
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
    
    def __eq__(self, other):
        return self.id == other.id


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        print(n)
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, s):
        visited = []
        queue = []
        s.color = 'gray'
        queue.append(s)
        while len(queue) > 0:
            u = queue.pop(0)
            visited.append(u)
            for v in u.getConnections():
                if v.color == 'white':
                    v.color = 'gray'
                    queue.append(v)
            u.color = 'black'
        return visited

    def depth_first_search(self):
        visited = []
        for vid in self.vertList:
            if self.vertList[vid].color == 'white':
                self.DFS(vid, visited)
        return visited

    def DFS(self, vid, visited):
        visited.append(self.vertList[vid])
        self.vertList[vid].color = 'gray'
        for v in self.vertList[vid].getConnections():
            if v.color == 'white':
                self.DFS(v.getId(), visited)
        self.vertList[vid].color = 'black'

if __name__ == '__main__':
    g = Graph()
    g.addVertex(0)
    print(g.getVertex(0))
    print(g.vertList)
    assert (g.getVertex(0) in g) == True
    # g = Graph()
    # for i in range(6):
    #     g.addVertex(i)
    #     g.addEdge(0,1)
    #     g.addEdge(0,5)
    #     g.addEdge(1,2)
    #     g.addEdge(2,3)
    #     g.addEdge(3,4)
    #     g.addEdge(3,5)
    #     g.addEdge(4,0)
    #     g.addEdge(5,4)
    #     g.addEdge(5,2)
    # for v in g:
    #     print(v)
    # assert (g.getVertex(0) in g) == True
    # assert (g.getVertex(6) in g) == False
    # print(g.getVertex(0))
    # assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'
    # print(g.getVertex(5))
    # assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'
    # path = g.breadth_first_search(0)
    # print('BFS traversal by discovery time (preordering): ', path)
    # assert path == [0, 1, 5, 2, 4, 3]
    # path = g.depth_first_search()
    # print('DFS traversal by discovery time (preordering): ', path)
    # assert path == [0, 1, 2, 3, 4, 5]