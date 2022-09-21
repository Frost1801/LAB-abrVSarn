import BST
import RBT


def main():
    tree = BST.BST()
    for x in range(0, 7, 1):
        tree.insert(x)
    tree.inorder()

    tree1 = RBT.RBT()
    for x in range(0, 7, 1):
        tree1.insert(x)
    tree1.inorder()



if __name__ == "__main__":
    main()
