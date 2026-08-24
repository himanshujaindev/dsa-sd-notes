class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, values):
        self.values = values
        self.root = None

    def build(self):
        if not self.values or self.values[0] is None:
            return None

        self.root = TreeNode(self.values[0])
        queue = [self.root]
        i = 1

        while queue and i < len(self.values):
            node = queue.pop(0)

            # left child
            if i < len(self.values):
                if self.values[i] is not None:
                    node.left = TreeNode(self.values[i])
                    queue.append(node.left)
                i += 1

            # right child
            if i < len(self.values):
                if self.values[i] is not None:
                    node.right = TreeNode(self.values[i])
                    queue.append(node.right)
                i += 1

        return self.root

    def print(self):
        # level-order print, similar in spirit to the adjacency list print
        if not self.root:
            print("Empty tree")
            return

        queue = [self.root]
        level = 0
        while queue:
            next_queue = []
            row = []
            for node in queue:
                if node:
                    row.append(node.val)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                else:
                    row.append(None)
            # stop once a level is all None
            if all(v is None for v in row):
                break
            print(f"{level}: {row}")
            queue = next_queue
            level += 1


if __name__ == "__main__":
    values = [3, 9, 20, None, None, 15, 7]

    tree = BinaryTree(values)
    tree.build()
    tree.print()
