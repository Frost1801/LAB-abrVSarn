import BST
import RBT
import Tester


def main():
    n = 1
    t = Tester.Tester()
    t.runTest(t.seqRelativePath, n, False)
    for i in range (0,10):
        t.runTest(t.randRelativePath, n, True)


if __name__ == "__main__":
    main()
