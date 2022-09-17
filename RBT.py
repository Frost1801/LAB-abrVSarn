

class NodoARN:  # rappresenta un nodo dell'albero binario di ricerca
    def __init__(self, key):  # costruttore della classe
        self.key = key
        self.left = None
        self.right = None
        self.root = None
        self.color = 0 # zero nero uno rosso
        # left e right sono dichiarati e inizializzati a null

    def getChildren(self):
        children = []
        if self.left != None:
            children.append(self.left)
        if self.right != None:
            children.append(self.right)
        return children

    # getter
    def get(self):
        return self.key

    def set(self, key):
        self.key = key

class ARN:
    def __init__(self):
        self.root = None
        self.NIL = NodoARN(None)

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


    def RBInsertFixup(self,node):
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
                    self.RightRotate(self, node.root.root)
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
                    self.LeftRotate(self, node.root.root)
        self.root.color = 0

    def LeftRotate (self, node):
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

    def RightRotate (self, node):
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
        def _inorder(v):
            if (v is self.NIL):
                return
            if (v.left is not self.NIL):
                _inorder(v.left)
            print(v.key, end="-")
            if (v.right is not self.NIL):\
                _inorder(v.right)

        _inorder(self.root)
