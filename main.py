import BST
import RBT
import Tester
import sys


def runTests(lower, upper):
    t = Tester.Tester()
    sys.setrecursionlimit(upper + 1000)  # serve per evitare errori dovuti alla ricorsione dell'albero
    for n in range(lower, upper):
        t.runTest(t.randRelativePath, n, True)
        t.runTest(t.seqRelativePath, n, False)

    print("Test completed")


def main():
    confirm = input("Press \"0\" to run the test, press any other key to cancel: ")
    if int(confirm) == 0:
        print("Starting test...")
        lower = 1
        upper = 1000
        runTests(lower, upper)
    else:
        print("Test cancelled")


if __name__ == "__main__":
    main()
