import BST


def main():
    tree = BST.ABR()
    tree.insert(4)
    tree.insert(5)
    for x in range(0, 70, 1):
        tree.insert(x)
    tree.inorder()


if __name__ == "__main__":
    main()
