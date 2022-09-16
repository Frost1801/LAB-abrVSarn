import BST


def main():
    tree = BST.ABR()
    tree.insert(4)
    tree.insert(5)
    for x in range(20, 10, -1):
        tree.insert(x)
    print(tree.find(5))
    print(tree.find(2))
    tree.inorder()


if __name__ == "__main__":
    main()
