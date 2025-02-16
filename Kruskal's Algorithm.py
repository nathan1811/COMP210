class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)


        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True # Successfully merged
        return False # Already in the same cycle
    
class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.edges = [] # (weight, u, v)

    def add_edge(self,u,v,weight):
        """Adding an edge between u and v with given weight"""
        self.edges.append((weight,u,v)) 

    def kruskal_mst(self):
        """Returning the Minimum Spanning Tree (MST)"""
        self.edges.sort() # Sorting the edges by their weights
        mst = [] # Storing the MST Edges
        ds = DisjointSet(self.V)

        for weight, u, v in self.edges:
            if ds.union(u,v): # If u and v are in different sets, add them to MST
                mst.append((u,v,weight))
            if len(mst) == self.V - 1: # Stop when we get V-1 Edges
                break
        return mst
    
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 7)
g.add_edge(3, 4, 9)
g.add_edge(4, 5, 10)
g.add_edge(3, 5, 8)
g.add_edge(2, 4, 5)

mst = g.kruskal_mst()
print("Edges in MST:", mst)
