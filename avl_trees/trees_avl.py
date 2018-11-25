"""
References:
https://www.cs.purdue.edu/homes/ayg/CS251/slides/chap7b.pdf
"""

from trees import Node
from trees_binary import BinaryTree


class AvlTree(BinaryTree):
    """Self-balancing AVL Trees"""

    def __init__(self):
        self.root = None


    def insert(self, key, value):
        # R child R subtree: Left rotation
        # L child L subtree: Right rotation
        # R child L subtree: Right-Left rotation
        # L child R subtree: Left-Right rotation)

        if self.root is None:
            self.root = Node(key, value)
            self.set_node_height(self.root)
        else:
            inserted_node = super(AvlTree, self).insert(key, value)
            self.set_node_height(inserted_node)

            # Start at the insertion Node
            self.rebalance(node_input=inserted_node)


    def rebalance(self, node_input):
        """Rebalance the AVL Tree by going from node_input to the root node, re-calculating
        the height as we go"""
        cur_node = node_input

        # Only rebalance if it is not the root
        while cur_node != self.root:
            # Go back up towards the root
            cur_node = cur_node.parent

            # Re-Set parent height
            self.set_node_height(node_input=cur_node)

            # If it is not balanced, do a rotation
            if not self.is_balanced(cur_node):
                taller_child = self.get_taller_child(cur_node)
                taller_grandchild = self.get_taller_child(taller_child)

                # If we went left on the child level
                child_went_left = taller_child.key <= cur_node.key
                # If we went left on the grandchild level
                grandchild_went_left = taller_grandchild.key <= taller_child.key

                if child_went_left and grandchild_went_left:
                    # If child and grandchild are both smaller than grandparent, perform
                    # one single right rotation
                    self.right_rotation(taller_grandchild)
                elif not child_went_left and not grandchild_went_left:
                    # If child and grandchild are both bigger than grandparent, perform
                    # one single left rotation
                    self.left_rotation(taller_grandchild)
                elif not child_went_left and grandchild_went_left:
                    # If child is bigger than grandparent, but grandchild is smaller than child,
                    # then perform a right-left rotation
                    self.right_left_rotation(taller_grandchild)
                elif child_went_left and not grandchild_went_left:
                    # If child is smaller than grandparent, but grandchild is bigger than child,
                    # then perform a left-right rotation
                    self.left_right_rotation(taller_grandchild)

                # Set heights for newly rotated nodes
                self.set_node_height(cur_node.left_child)
                self.set_node_height(cur_node.right_child)
                self.set_node_height(cur_node)


    def left_rotation(self, node_input):
        """
        Perform a left rotation

        # ARGUMENTS
        node_input  -> the grandchild node to balance
        """
        # TODO: Need to add edge cases!
        parent = node_input.parent
        grandparent = parent.parent

        # Rotate left
        temp_left_child = parent.left_child
        parent.left_child = grandparent
        parent.parent = grandparent.parent
        if parent.parent is not None:
            left_c = self.is_left_child(parent)
            if left_c:
                parent.parent.left_child = parent
            else:
                parent.parent.right_child = parent
        else:
            self.root = parent

        grandparent.parent = parent
        grandparent.right_child = temp_left_child
        if temp_left_child is not None:
            temp_left_child.parent = grandparent

        # Return the "root" node
        return parent


    def right_rotation(self, node_input):
        """
        Perform a right rotation

        # ARGUMENTS
        node_input  -> node to rebalance.
        """
        # TODO: Need to add edge cases!
        parent = node_input.parent
        grandparent = parent.parent

        # Rotate right
        temp_right_child = parent.right_child
        parent.right_child = grandparent
        parent.parent = grandparent.parent
        if parent.parent is not None:
            left_c = self.is_left_child(parent)
            if left_c:
                parent.parent.left_child = parent
            else:
                parent.parent.right_child = parent
        else:
            self.root = parent

        grandparent.parent = parent
        grandparent.left_child = temp_right_child
        if temp_right_child is not None:
            temp_right_child.parent = grandparent

        # Return the "root" node
        return parent


    def right_left_rotation(self, node_input):
        """
        Perform a right-left rotation on node_input, its parent, and its grandparent

        # ARGUMENTS
        node_input  -> The grandchild node.
        """
        parent = node_input.parent
        grandparent = parent.parent

        # node_input's original children
        init_node_left = node_input.left_child
        init_node_right = node_input.right_child

        # Rotate!
        node_input.left_child = grandparent
        node_input.right_child = parent
        node_input.parent = grandparent.parent

        if node_input.parent is not None:
            left_c = self.is_left_child(node_input)
            if left_c:
                node_input.parent.left_child = node_input
            else:
                node_input.parent.right_child = node_input
        else:
            self.root = node_input

        # Rotate the other children nodes
        grandparent.parent = node_input
        parent.parent = node_input

        grandparent.right_child = init_node_left
        if init_node_left is not None:
            init_node_left.parent = grandparent

        parent.left_child = init_node_right
        if init_node_right is not None:
            init_node_right.parent = parent

        # Return the new "root" node of this subtree
        return node_input


    def left_right_rotation(self, node_input):
        """
        Perform a left-right rotation on node_input, its parent, and its grandparent

        # ARGUMENTS
        node_input  -> The grandchild node.
        """
        parent = node_input.parent
        grandparent = parent.parent

        # node_input's original children
        init_node_left = node_input.left_child
        init_node_right = node_input.right_child

        # Rotate!
        node_input.left_child = parent
        node_input.right_child = grandparent
        node_input.parent = grandparent.parent

        # Set node_input to replace grandparent node as child node
        if node_input.parent is not None:
            left_c = self.is_left_child(node_input)
            if (left_c):
                node_input.parent.left_child = node_input
            else:
                node_input.parent.right_child = node_input
        else:
            # We are at the root node
            self.root = node_input

        parent.parent = node_input
        grandparent.parent = node_input

        parent.right_child = init_node_left
        if parent.right_child is not None:
            parent.right_child.parent = parent

        grandparent.left_child = init_node_right
        if grandparent.left_child is not None:
            grandparent.left_child.parent = grandparent

        # Return the new "root" node of this subtree
        return node_input


    def get_height_fn(self, node_input):
        """Recursively get the height of the node_input"""
        if node_input is None:
            height = 0
        else:
            height = node_input.height

        return height


    def set_node_height(self, node_input):
        """set node_input's height"""
        if node_input is not None:
            left_height = self.get_height_fn(node_input.left_child)
            right_height = self.get_height_fn(node_input.right_child)
            max_height = max(left_height, right_height)

            # Set the node_input's height
            node_input.set_height(1 + max_height)


    def is_balanced(self, node_input):
        """Test whether node node_input has a balance factor between -1 and 1.
        If the balance factor is outside this range, the tree is unbalanced. We
        are doing this by getting the height difference between the left subtree
        and the right subtree."""
        bal_factor = self.get_height_fn(node_input.left_child) - self.get_height_fn(node_input.right_child)
        return bal_factor >= -1 and bal_factor <= 1


    def get_taller_child(self, node_input):
        """Obtain a child of node_input with height >= other child's height"""
        left_height = self.get_height_fn(node_input.left_child)
        right_height = self.get_height_fn(node_input.right_child)

        if left_height >= right_height:
            return node_input.left_child
        else:
            return node_input.right_child


    def is_left_child(self, node_input):
        """
        Determine if the node_input is a left or a right child. Node_input MUST
        have a parent (a.k.a. it is NOT the root node)

        # ARGUMENTS
        node_input  -> The child input that you want to determine if it is the
                        left or right child

        # RETURNS
        True if it is a left child, False if it is a right child.
        """
        parent = node_input.parent
        if parent is not None:
            return node_input <= parent
        else:
            raise ValueError("Parent node does not exist")
