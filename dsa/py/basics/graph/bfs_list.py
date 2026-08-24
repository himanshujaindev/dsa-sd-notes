from collections import deque

from dsa.py.basics.graph.graph_builder import *


def bfs_iterative(adj, start_node):
    visited = [False] * len(adj)
    order = []
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        order.append(node)

        for next_node in adj[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return order


if __name__ == "__main__":
    n = 4  # number of nodes
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    graph = AdjacencyList(n, edges)
    adj = graph.build()
    graph.print()
    print("\n\n")
    print(bfs_iterative(adj, 3))
