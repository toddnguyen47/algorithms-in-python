from trees import Tree


class AvlTrees(Tree):
    """Self-balancing AVL Trees"""

    def __init__(self):
        self.root = None


    def insert(self, key, value):
        # R child R subtree: Left rotation
        # L child L subtree: Right rotation
        # R child L subtree: Right-Left rotation
        # L child R subtree: Left-Right rotation)

        # If the root is empty
        if self.root is None:
            self.root = Node(key, value, height=0)
        # Else
        else:
            # Add to tree
            node_added = self.add_to_tree(key, value)

            # Rebalance tree


    def left_rotation(self, node_input):
        """
        Perform a left rotation

        # ARGUMENTS
        node_input  -> node to rebalance.
        """
        # TODO: Need to add edge cases!
        parent = node_input.parent
        grandparent = parent.parent

        # Rotate left
        parent.left_child = grandparent
        grandparent.parent = parent

        # Update heights

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
        parent.right_child = grandparent
        grandparent.parent = parent

        # Update heights

        # Return the "root" node
        return parent


    def get_height_fn(self, node_input):
        if node_input is None:
            height = 0
        else:
            # Recursively get the height
            left_height = self.get_height_fn(node_input.left_child)
            right_height = self.get_height_fn(node_input.right_child)
            height = max(left_height, right_height)

        return height


    def add_to_tree(self, key, value):
        """
        Binary-li traverse the tree then where we can add the node.
        NOTE: This only works if self.root is NOT None.

        # ARGUMENTS
        key     -> key to add
        value   -> value

        # RETURNS
        The newly added node
        """
        cur_node = self.root
        prev_node = None
        went_left = False

        while (cur_node is not None):
            went_left = False
            prev_node = cur_node
            key_compared = key - cur_node.key
            # If key is less than or equal to key to add then go left
            if key_compared <= 0:
                cur_node = cur_node.left_child
                went_left = True
            # Else go right
            else:
                cur_node = cur_node.right_child
                went_left = False

        # Add
        cur_node = Node(key, value, height=prev_node.height + 1)
        cur_node.parent = prev_node

        if (went_left):
            prev_node.left_child = cur_node
        else:
            prev_node.right_child = cur_node

        # Update prev_node height

        return cur_node
