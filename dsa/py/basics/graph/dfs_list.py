from dsa.py.basics.graph.graph_builder import *


def dfs_iterative(adj, start_node):
    visited = [False] * len(adj)
    order = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if visited[node]:
            continue

        order.append(node)
        visited[node] = True

        for next_node in adj[node]:
            if not visited[next_node]:
                stack.append(next_node)

    return order


def dfs_recursive(adj, start_node):
    visited = [False] * len(adj)
    order = []

    def _visit(node: int) -> None:
        visited[node] = True
        order.append(node)
        for next_node in adj[node]:
            if not visited[next_node]:
                _visit(next_node)

    _visit(start_node)
    return order


if __name__ == "__main__":
    n = 4  # number of nodes
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    graph = AdjacencyList(n, edges)
    adj = graph.build()
    graph.print()
    print("\n\n")
    print(dfs_recursive(adj, 3))
    print(dfs_iterative(adj, 3))
