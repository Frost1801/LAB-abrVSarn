class Node:  # rappresenta un nodo dell'albero binario di ricerca
    def __init__(self, key):  # costruttore della classe
        self.key = key
        self.left = None
        self.right = None
        self.root = None
        # left e right sono dichiarati e inizializzati a null

    def getChildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    # getter
    def get(self):
        return self.key

    def set(self, key):
        self.key = key


class BST:  # rappresenta un albero binario di ricerca
    def __init__(self):
        self.root = None

    # imposta la radice
    def setRoot(self, key):
        self.root = Node(key)

    # metodo per inserire un valore nell'albero
    def insert(self, key):
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        node = Node(key)
        node.root = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    # visita l'albero in ordine crescente
    def inorder(self):
        def _inorder(v):
            if v is None:
                return
            if v.left is not None:
                _inorder(v.left)
            print(v.key, end="-")
            if v.right is not None:
                _inorder(v.right)

        _inorder(self.root)


    #FIXME
    def height (self):
        def _height(root):
            # controlla se l'albero è vuoto
            if root is None:
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