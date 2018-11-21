import unittest
import trees_avl


class TestAvlTrees(unittest.TestCase):
    def testNode(self):
        # Test if adding nodes is correct
        tempNode = trees_avl.Node(5, "10", 0)
        self.assertEqual(5, tempNode.key)
        self.assertEqual("10", tempNode.value)

        # Test if adding nodes is correct
        tempNode = trees_avl.Node("10", 5, 0)
        self.assertEqual("10", tempNode.key)
        self.assertEqual(5, tempNode.value)


    def testLeftRotation(self):
        """
        Test if left rotation is correct
        """
        avl_tree = trees_avl.AvlTrees()
        grandparent = trees_avl.Node(4, 4, 0)
        parent = trees_avl.Node(6, 6, 1)
        child = trees_avl.Node(8, 8, 2)

        grandparent.right_child = parent
        parent.parent = grandparent

        parent.right_child = child
        child.parent = parent

        avl_tree.left_rotation(child)
        self.assertEqual(parent.left_child.key, grandparent.key)


    def testRightRotation(self):
        """
        Test if right rotation is correct
        """
        avl_tree = trees_avl.AvlTrees()
        grandparent = trees_avl.Node(8, 8, 0)
        parent = trees_avl.Node(6, 6, 1)
        child = trees_avl.Node(4, 4, 2)

        grandparent.left_child = parent
        parent.parent = grandparent

        parent.left_child = child
        child.parent = parent

        avl_tree.right_rotation(child)
        self.assertEqual(parent.right_child.key, grandparent.key)


    def testGetHeight(self):
        avl_tree = trees_avl.AvlTrees()
        """Test if get_height() is correct"""
        self.assertEqual(avl_tree.get_height(None), 0)

        avl_tree.insert(10, 15)
        self.assertEqual(avl_tree.get_height(avl_tree.root), 0)


    def testAddToTree(self):
        """Test if we can add to the tree"""
        avl_tree = trees_avl.AvlTrees()

        avl_tree.insert(10, 15)
        root = avl_tree.root
        self.assertEqual(root.key, 10)
        self.assertEqual(root.height, 0)

        cur_node = avl_tree.add_to_tree(5, 5)
        self.assertEqual(root.left_child.key, cur_node.key)
        self.assertEqual(root.left_child.height, 1)

        cur_node = avl_tree.add_to_tree(20, 20)
        self.assertEqual(root.right_child.key, cur_node.key)
        self.assertEqual(root.right_child.height, 1)

        cur_node = avl_tree.add_to_tree(8, 8)
        self.assertEqual(root.left_child.right_child.key, cur_node.key)
        self.assertEqual(root.left_child.right_child.height, 2)
