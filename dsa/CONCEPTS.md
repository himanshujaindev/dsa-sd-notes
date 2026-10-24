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

---
CONCEPTS.md
arrays
- Hashing
- Hashset
- Two pointers
- prefix and sufix
- Kadane's Algorithm
- sorted - binary search

---

Sliding Window Time Complexity:
Nested loops usually mean O(n²) because the inner loop restarts from scratch each time the outer loop moves. In sliding window, the inner loop never restarts. It continues from wherever l left off.
If both pointers only move forward and each is bounded by n, total movement is at most n + n = 2n, so the algorithm is O(n), regardless of how many loops are written.

does the left pointer ever reset or move backward?
- No → O(n)
- Yes (e.g., it jumps back to the start each time) → likely O(n²)

Think of the window as a caterpillar crawling along the array:
- The right edge (r) moves forward one step at a time, from 0 to n. That’s n moves.
- The left edge (l) only moves forward too, and can never go past the end. That’s at most n moves.
Total work = n (outer) + n (inner, at most) = 2n → O(n).

The while loop looks like extra work stacked on top of the for loop, but it isn’t restarting. It just advances l, and l has a fixed budget of n steps for the entire algorithm, not n steps per outer iteration.

---

dp
Recursion -> Memoization -> Tabulation -> Space Optimization

Two properties of dp problem:
Optimal Substructure -> Problem can be expressed in terms of Recursion
Overlapping Subproblems -> Many subproblems that are computed multiple times

Memoization (recursion) = Top-down = main problem -> base case

Steps:
1. create dp[n+1] array initialized to -1
2. if(dp[n] != -1) -> return dp[n] // value is already computed
3. else -> use recursive relation to compute dp[n] -> at the end, store the result


Tabulation = Bottom-up = base case -> main problem

Steps:
1. declare dp[n+1] array
2. initialize the base case -> dp[0] and/or dp[1]
3. traverse array -> every index -> dp[i] = dp[i-1] + dp[i-2]


Space Optimization

Steps:
1. If additional space is not required, use variables
    dp[i-1] -> prev1
    dp[i-2] -> prev2


---


sorting
1. selection sort - find min and swap
2. bubble sort - swap locally by moving largest element to the end
3. quick sort - pivot (partition) -> 1st element; i -> more than pivot; j -> less than pivot; swap
4. Merge sort - merge two sorted array
5. insertion sort - 1st element is sorted; every time 1 element is inserted into sorted arr
6. heap sort - 
7. selection sort

---

search
1. linear search
2. binary search - low, mid, high

---

Linked List:
- Use pointers
- Use dummy nodes

---

graph:
1. dfs - stack
2. bfs - queue (Shortest Path)
3. directed acyclic graph (DAG) -
    topological sorting - dfs -> reverse pop

adjacent matrix
adjacent list - for every vertex - all edges


shortest path in graph
single source shortest path

---

tree: Solve by recursion
1. binary tree (1 parent - 2 child)
    hieght: max(height(left), height(right)) + 1
            count number of edges
            node to leaf
    depth = level = node to root

BT -> Heap
BST -> AVL -> BTT -> 2-3 tree (B Tree)

AVL
- Balanced BST
- Balancing Factor (BF) = Height of Left Subtree - Height of Right Subtree
- AVL is balanced if BF = 0, 1 or -1



Insertion of node
Deletion of node


Spanning Tree - Convert Graph -> Tree

Preoder - root, left, right
Inorder - left, root, right
Postorder - left, right, root











Travelling Salesman Problem (TSP)
Knapsack Problem
Job Assignment Problem
Divide and Conquer
Decrease and Conquer - divide into two; discard one piece
Fake Coin Problem

heap - find kth smallest elem
- tree (complete BT)
- parental domination
p -> left child = 2p+1; right child = 2p+2
last parent -> (n/2)-1 ; n = # nodes
min heap; max heap

--------


Floyd Warshall Algo
- All pair shortest path
- Generate shortestPathMatrix
- Intermediate node - k
```
For k = 0 to n – 1 
    For i = 0 to n – 1 
        For j = 0 to n – 1 
            Distance[i, j] = min(Distance[i, j], Distance[i, k] + Distance[k, j])
where i = source Node, j = Destination Node, k = Intermediate Node
```


---- BD

Dijkstra's Algo
- Single source shortest path
- Unweighted graph
- Greedy method
- Create shortest path tree (SPT) with given source as root
- maintain 2 set
    one set contains vertices included in SPT
    another set contains vertices not included in SPT
- {0 INF INF INF INF INF} -> update this with weight
- {0 ... } -> SPT


Bellman Ford
- Single source shortest path
- Weight graph / Detect Negative edges
- distance array and edges list
- A -> B = 3 ; d(A) + 3 = d(B)
- Iterate thro all the edges (v-1) times
- if relaxation for vth time is possible then negative weight cycle is detected

-----

Minimum Spanning Tree (PK)
- Prim's Algo
1. pick any start vertex
2. identify fringe vertex (vertex connected to the cur vertex)
3. pick the smallest edge
4. add to the tree if it does not form cycle


- Kruskal's Algo
1. sort the edges
2. pick smallest edge
   if no cycle, then add the edge
3. (v-1) edges


1. Count Number of Islands
2. Word Search - Backtracking
3. All the paths from source to destination = dfs + backtracking




https://www.aboutamazon.in/about-us/leadership-principles

