class Node(object):
    def __init__(self, value):
        self.value = value
        self.right_son = None
        self.left_son = None
        self.height = 1

class AVL_Tree(object):
    def insert(self, root, value):
        ## if insert node into the empty tree
        if root is None:
            return Node(value)
        
        ## else, determine where the node should be and insert it into the tree
        else:
            if root.value > value:
                root.left_son = self.insert(root.left_son, value)
            else:
                root.right_son = self.insert(root.right_son, value)

        ## update height of father node, i.e root
        root.height = 1 + max(self.getHeight(root.left_son), self.getHeight(root.right_son))

        balance = self.getBalance(root)

        ## LL
        if balance > 1 and value < root.left_son.value:
            return self.rotateRight(root)
        
        ## RR
        if balance < -1 and value >= root.right_son.value:
            return self.rotateLeft(root)
        
        ## LR
        ## turn it back to LL by rotating to the Left the left child
        if balance > 1 and value >= root.left_son.value:
            root.left_son = self.rotateLeft(root.left_son)
            return self.rotateRight(root)
        
        ## RL
        ## turn it back to RR by rotating to the right the right child
        if balance < -1 and value < root.right_son.value:
            root.right_son = self.rotateRight(root.right_son)
            return self.rotateLeft(root)
        
        return root
    
    def rotateLeft(self, node):
        newFather = node.right_son
        newSon = newFather.left_son

        newFather.left_son = node
        node.right_son = newSon

        node.height = 1 + max(self.getHeight(node.left_son), self.getHeight(node.right_son))
        newFather.height = 1 + max(self.getHeight(newFather.left_son), self.getHeight(newFather.right_son))

        return newFather
    
    def rotateRight(self, node):
        newFather = node.left_son
        newSon = newFather.right_son

        newFather.right_son = node
        node.left_son = newSon

        node.height = 1 + max(self.getHeight(node.left_son), self.getHeight(node.right_son))
        newFather.height = 1 + max(self.getHeight(newFather.left_son), self.getHeight(newFather.right_son))

        return newFather
    
    def getHeight(self, root):
        if root is None:
            return 0
        return root.height
    
    def getBalance(self, root):
        if root is None:
            return 0
        return self.getHeight(root.left_son) - self.getHeight(root.right_son)