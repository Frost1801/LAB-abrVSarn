import BST
import RBT


def main():
    tree = BST.ABR()
    for x in range(0, 7, 1):
        tree.insert(x)
    tree.inorder()

    tree = RBT.ARN()
    for x in range(0, 7, 1):
        tree.insert(x)
    tree.inorder()


if __name__ == "__main__":
    main()
