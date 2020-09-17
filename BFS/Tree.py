class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self, nodeList):
        self.root = None
        self.queue = []
        self.nodeList = nodeList
        self.structure = []

    def construct(self):
        for item in self.nodeList:
            node = TreeNode(item)
            if self.root is None:
                self.root = node
                self.structure.append(node)
                self.queue.append(self.root)
            else:
                treenode = self.queue[0]
                if treenode.left is None:
                    self.structure.append(node)
                    treenode.left = node
                    self.queue.append(treenode.left)
                else:
                    treenode.right = node
                    self.structure.append(node)
                    self.queue.append(treenode.right)
                    self.queue.pop(0)

    def bfs(self):
        order = []
        if self.root is None:
            return order

        q = []
        q.append(self.root)
        while len(q) != 0:
            length = len(q)
            for i in range(length):
                r = q.pop(0)
                if r.left is not None:
                    q.append(r.left)
                if r.right() is Not None:
                    q.append(r.right)
                order.append(r.val)
                print(r.val)
        return order
