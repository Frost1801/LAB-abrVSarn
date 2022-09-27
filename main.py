import BST
import RBT
import Tester


def main():
    lower = 1
    upper = 100
    t = Tester.Tester()

    for n in range (lower, upper):
        t.runTest(t.randRelativePath, n, True)
        t.runTest(t.seqRelativePath, n, False)


if __name__ == "__main__":
    main()
