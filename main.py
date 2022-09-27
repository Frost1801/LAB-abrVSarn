import BST
import RBT


def fillTree(tree, n):
    for x in range(0, n, 1):
        tree.insert(x)
    return tree


def main():
    n = 9
    tree = BST.BST()
    tree = fillTree(tree, n)
    tree.inorder()
    print("\n" + str(tree.root.height()) + "\n")

    tree1 = RBT.RBT()
    tree1 = fillTree(tree1, n)
    tree1.inorder()
    print("\n" + str(tree1.root.height()) + "\n")

    tree2 = BST.BST()
    tree3 = RBT.RBT()
    try:
        print("\n" + str(tree2.root.height()) + "\n")
        print("\n" + str(tree3.root.height()) + "\n")
    except AttributeError:
        print("Called on tree with 0 nodes")


if __name__ == "__main__":
    main()
