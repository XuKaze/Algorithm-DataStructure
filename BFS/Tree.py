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

    def construct(self):
        for item in nodeList:
            node = TreeNode(item)
            if self.root is None:
                self.root = node
                self.queue.append(self.root)
            else:
                treenode = self.queue[0]
                if treenode.left is None:
                    treenode.left = node
                    self.queue.append(treenode.left)
                else:
                    treenode.right = node
                    self.queue.append(treenode.right)
                    self.queue.pop(0)



node_List = [5,1,4,None,None,3,6]

A = Tree(node_List)
