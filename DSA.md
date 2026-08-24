Data Structures & Algos
1. Arrays: 
    - Operations:
        - Insert: O(n)
        - Access: O(1)
        - Search: O(n)
        - Delete: O(n)

    - Patterns & Problems:
        - Two Pointers
        - Sliding Window
        - Binary Search
        - Prefix/Suffix Sum

    - Sorting
        - Selection sort
        - Insertion sort
        - Merge sort
        - Quick sort
        - Bubble sort

    - Algos:
        - Kadane's Algo
        - Merge Interval


2. Strings
    - Patterns & Problems:
        - Pattern Searching
        - String Builder
        - Longest substring


3. HashTable (Hashmap/Hashset): 
    - Operations:
        - Insert: O(1) avg, O(n) worst
        - Search: O(1) avg, O(n) worst
        - Delete: O(1) avg, O(n) worst


4. Matrix


5. Linked List
    - Operations:
        - Insert (at known node): O(1) | Insert (at position i): O(n)
        - Access: O(n)
        - Search: O(n)
        - Delete (at known node): O(1)

    - Patterns & Problems:
        - Reversal
        - Detect cycle
        - Find middle
        - Merge sorted LL
        - Remove Nth node


6. Stack
    - Operations:
        - Push: O(1) | Pop: O(1) | Peek: O(1) | Search: O(n)


7. Queue
    - Operations:
        - Enqueue: O(1) | Dequeue: O(1) | Peek: O(1) | Search: O(n)


8. Trees
    - Traversal
        - Inorder: left <u>root</u> right
        - Preorder: <u>root</u> left right
        - Postorder: left right <u>root</u>
    - Level order traversal = BFS on BT
    - Heigth / Depth
    - Diameter
    - Invert binary tree
    - Lowest common ancestor
    - Binary search tree (BST): Insert: O(n) worst, O(log n) avg | Delete: O(n) worst | Search: O(n) worst
    - Balanced BST (AVL): Insert: O(log n) | Delete: O(log n) | Search: O(log n)


Binary Tree (BT): Each node can have at most two children
Types of Binary Tree:
    On the basis of Number of Children
        - Full Binary Tree
        - Degenerate Binary Tree
        - Skewed Binary Trees
    On the basis of Completion of Levels
        - Complete Binary Tree
        - Perfect Binary Tree
        - Balanced Binary Tree
    On the basis of Node Values:
        - Binary Search Tree:
            - left subtree contains values smaller than the parent node and right subtree contains values greater than the parent node
        - AVL Tree
        - Red Black Tree
        - B Tree
        - B+ Tree
        - Segment Tree

Properties:
Number of Edges: A tree with N nodes always has N − 1 edges. There is exactly one unique path between any two nodes in a tree.
Depth of a Node: The depth of a node is the number of edges from the root node to that node. The root node always has a depth of 0.
Height of a Node: The height of a node is the number of edges on the longest path from that node to any leaf node.
Height of a Tree: The height of a tree is the height of its root node, which is equal to the number of edges on the longest path from the root to a leaf node.
Degree of a Node: The degree of a node is the number of children it has. A leaf node always has a degree of 0.
Degree of a Tree: The degree of a tree is the highest degree among all the nodes in the tree.



9. Graph
    - Representation:
        - Adj List: Add vertex: O(1) | Add edge: O(1) | Remove edge: O(E) | Time: O(V+E)
        - Adj Matrix: Add edge: O(1) | Remove edge: O(1) | Check edge: O(1) | Time: O(V²)
    - BFS (Queue) | Space: O(V)
    - DFS (Stack) | Space: O(V)
    
    - Patterns & Problems:
        - Detect cycle
        - Topological sort
        - Dijkstra's Algo
        - Shortest path

Algo:
Dijkstra’s shortest path: weighted undirected graph, Min Priority Queue

10. Greedy
    - Patterns & Problems:
        - Activity selection
        - Fractional Knapsack
        - Huffman Coding
        - Minimum Spanning Tree

11. Heap / Priority Queue
    - Operations:
        - Insert: O(log n)
        - Delete-min/max: O(log n)
        - Peek min/max: O(1)
        - Build heap: O(n)

    - Patterns & Problems:
        - Min Heap
        - Max Heap
        - Kth largest/smallest
        - Heap Sort

12. Recursion
13. Backtracking
14. Dynamic Programming
15. Bit Manipulation
16. Adv Topics
    - Tries
    - Segment trees
    - Union Find