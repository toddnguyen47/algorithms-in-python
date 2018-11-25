from trees_avl import AvlTree
from trees_binary import BinaryTree


if __name__ == "__main__":
    # avl_trees = AvlTree()
    # binary_tree = BinaryTree()
    binary_tree = AvlTree()

    binary_tree.printTree()
    # print(binary_tree.getValue(20))
    # binary_tree.insert(20, 20)
    # binary_tree.printTree()
    # binary_tree.insert(25, 25)
    # binary_tree.printTree()
    # binary_tree.insert(15, 15)
    # binary_tree.printTree()
    # binary_tree.insert(30, 30)
    # binary_tree.printTree()
    # binary_tree.insert(40, 40)
    # binary_tree.insert(30, 30)
    # binary_tree.insert(24, 24)
    # binary_tree.insert(27, 27)
    # binary_tree.insert(26, 26)
    # print(binary_tree.getValue(20))
    # print(binary_tree.getValue(26))

    # # Test single left rotation
    # binary_tree.insert(4, 4)
    # binary_tree.insert(2, 2)
    # binary_tree.insert(14, 14)
    # binary_tree.insert(12, 12)
    # binary_tree.insert(24, 24)
    # binary_tree.insert(22, 22)
    # binary_tree.insert(26, 26)


    # Test single right rotation
    # binary_tree.insert(24, 24)
    # binary_tree.insert(30, 30)
    # binary_tree.insert(14, 14)
    # binary_tree.insert(19, 19)
    # binary_tree.insert(4, 4)
    # binary_tree.insert(2, 2)

    # Test right-left rotation
    binary_tree.insert(4, 4)
    binary_tree.insert(2, 2)
    binary_tree.insert(24, 24)
    binary_tree.insert(14, 14)
    binary_tree.insert(30, 30)
    binary_tree.insert(10, 10)
    binary_tree.insert(18, 18)
    binary_tree.printTree()
    binary_tree.clear()
    print("\nAfter Clearing...\n")

    # Test left-right rotation
    binary_tree.insert(24, 24)
    binary_tree.insert(4, 4)
    binary_tree.insert(30, 30)
    binary_tree.insert(2, 2)
    binary_tree.insert(14, 14)
    binary_tree.insert(10, 10)
    binary_tree.insert(18, 18)
    binary_tree.printTree()
