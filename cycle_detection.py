from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)
        
    def isCyclicUtil(self, v, visited, parent):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            elif parent != i:
                return True
        return False
    
    def isCyclic(self):
        counter=int(0)
        visited=[False]*(self.v)
        for i in range(self.v):
            if visited[i]==False:
                if(self.isCyclicUtil(i,visited,-1)==True):
                    counter=counter+1
        return counter
    


g = Graph(7)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(1, 3)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(4, 6)
g.addEdge(1, 7)



output=g.isCyclic()
print("graph one")
if output:
    print(output)
else:
    print("Graph does not contain cycle ")
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
 
print("graph two")
if(g1.isCyclic()):
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
