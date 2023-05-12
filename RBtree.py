class Node():
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_son = None
        self.right_son = None
        self.color = 'red'

class RB_Tree():
    def __init__(self):
        self.leaf = Node(0)
        self.leaf.color = 'black'
        self.leaf.left_son = None
        self.leaf.right_son = None
        self.root = self.leaf

    # Balance the tree after insertion
    def fix_insert(self, k):
        ##  if dad is RED
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right_son:
                u = k.parent.parent.left_son
                ## if uncle is RED
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left_son:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right_son

                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right_son:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right_son
        x.right_son = y.left_son
        if y.left_son != self.leaf:
            y.left_son.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left_son:
            x.parent.left_son = y
        else:
            x.parent.right_son = y
        y.left_son = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left_son
        x.left_son = y.right_son
        if y.right_son != self.leaf:
            y.right_son.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right_son:
            x.parent.right_son = y
        else:
            x.parent.left_son = y
        y.right_son = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.value = key
        node.left_son = self.leaf
        node.right_son = self.leaf
        node.color = 'red'

        y = None
        x = self.root

        while x != self.leaf:
            y = x
            if node.value < x.value:
                x = x.left_son
            else:
                x = x.right_son

        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left_son = node
        else:
            y.right_son = node

        if node.parent == None:
            node.color = 'black'
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root
    
    def getHeight(self, root):
        if root is None:
            return 0
        else:
            leftHeight = self.getHeight(root.left_son)
            rightHeight = self.getHeight(root.right_son)
            return max(leftHeight, rightHeight) + 1
