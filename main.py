import BST
import RBT


def main():
    n = 1
    tree = BST.BST()
    for x in range(0, n, 1):
        tree.insert(x)
    tree.inorder()
    print("\n" + str(tree.height()) + "\n")
    print("\n" + str(tree.depth()) + "\n")

    tree1 = RBT.RBT()
    for x in range(0, n, 1):
        tree1.insert(x)
    tree1.inorder()
    print("\n" + str(tree1.height()) + "\n")
    print("\n" + str(tree1.depth()) + "\n")

    tree2 = BST.BST()
    tree3 = RBT.RBT()
    print("\n" + str(tree2.height()) + "\n")
    print("\n" + str(tree2.depth()) + "\n")
    print("\n" + str(tree3.height()) + "\n")
    print("\n" + str(tree3.depth()) + "\n")


if __name__ == "__main__":
    main()
