from trees_avl import AvlTrees
from trees_binary import BinaryTree


if __name__ == "__main__":
    avl_trees = AvlTrees()
    binary_tree = BinaryTree()

    binary_tree.printTree()
    print(binary_tree.getValue(20))
    binary_tree.insert(20, 20)
    binary_tree.insert(25, 25)
    binary_tree.insert(15, 15)
    binary_tree.insert(10, 10)
    binary_tree.insert(30, 30)
    binary_tree.insert(24, 24)
    binary_tree.insert(27, 27)
    binary_tree.insert(26, 26)
    print(binary_tree.getValue(20))

    binary_tree.printTree()
