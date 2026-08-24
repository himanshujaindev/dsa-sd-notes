class AdjacencyMatrix:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.matrix = [[0 for i in range(self.n)] for _ in range(self.n)]

    def add_edge(self, edge):
        self.matrix[edge[0]][edge[1]] = 1  # unweighted
        self.matrix[edge[1]][edge[0]] = 1  # undirectional (undirected)

    def build(self):
        for edge in self.edges:
            self.add_edge(edge)
        return self.matrix

    def print(self):
        for row in self.matrix:
            print(row)


class AdjacencyList:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.adjList = [[] for _ in range(self.n)]

    def add_edge(self, edge):
        self.adjList[edge[0]].append(edge[1])
        self.adjList[edge[1]].append(edge[0])  # undirectional (undirected)

    def build(self):
        for edge in self.edges:
            self.add_edge(edge)
        return self.adjList

    def print(self):
        for i, row in enumerate(self.adjList):
            print(f"{i}: {row}")


if __name__ == "__main__":
    n = 4  # number of nodes
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    graph = AdjacencyMatrix(n, edges)
    graph.build()
    graph.print()

    print("\n\n")

    graph = AdjacencyList(n, edges)
    graph.build()
    graph.print()
