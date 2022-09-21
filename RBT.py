import BST


class NodoARN(BST.Node):  # rappresenta un nodo dell'albero binario di ricerca
    def __init__(self, key):
        super().__init__(key)
        self.color = 0  # zero nero uno rosso


class RBT:
    def __init__(self):
        self.NIL = NodoARN(None)
        self.root = self.NIL

    # imposta la radice
    def setRoot(self, key):
        self.root = NodoARN(key)

    # metodo per inserire un valore nell'albero
    def insert(self, key):
        y = self.NIL
        x = self.root
        while x is not self.NIL:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        node = NodoARN(key)
        node.root = y
        if y is self.NIL:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        node.left = self.NIL
        node.right = self.NIL
        node.color = 1
        self.RBInsertFixup(node)

    def RBInsertFixup(self, node):
        while node.root.color == 1:
            if node.root == node.root.root.left:
                y = node.root.root.right
                if y.color == 1:
                    node.root.color = 0
                    y.color = 0
                    node.root.root.color = 1
                    node = node.root.root
                else:
                    if node == node.root.right:
                        node = node.root
                        self.LeftRotate(self, node)
                    node.root.color = 0
                    node.root.root.color = 1
                    self.RightRotate(node.root.root)
            else:
                y = node.root.root.left
                if y.color == 1:
                    node.root.color = 0
                    y.color = 0
                    node.root.root.color = 1
                    node = node.root.root
                else:
                    if node == node.root.left:
                        node = node.root
                        self.RightRotate(self, node)
                    node.root.color = 0
                    node.root.root.color = 1
                    self.LeftRotate(node.root.root)
        self.root.color = 0

    def LeftRotate(self, node):
        y = node.right
        node.right = y.left
        if y.left is not self.NIL:
            y.left.root = node
        y.root = node.root
        if node.root is self.NIL:
            self.root = y
        elif node == node.root.left:
            node.root.left = y
        else:
            node.root.right = y
        y.left = node
        node.root = y

    def RightRotate(self, node):
        y = node.left
        node.left = y.right
        if y.right is not self.NIL:
            y.right.root = node
        y.root = node.root
        if node.root is self.NIL:
            self.root = y
        elif node == node.root.right:
            node.root.right = y
        else:
            node.root.left = y
        y.right = node
        node.root = y

    def inorder(self):
        print()

        def _inorder(v):
            if v is self.NIL:
                return
            if v.left is not self.NIL:
                _inorder(v.left)
            print(v.key, end="-")
            if v.right is not self.NIL:
                _inorder(v.right)

        _inorder(self.root)
    #FIXME
    def height (self):
        def _height(root):
            # controlla se l'albero è vuoto
            if root is self.NIL:
                return 0

            leftAns = _height(root.left)
            rightAns = _height(root.right)
            return max(leftAns, rightAns) + 1
        return _height(self.root)

    def depth(self):
        def _depth (root):
            left_depth = root.left.depth() if root.left else 0
            right_depth = root.right.depth() if root.right else 0
            return max(left_depth, right_depth) + 1
        return _depth(self.root)