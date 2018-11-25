from trees import Tree, Node
from datetime import datetime


class BinaryTree(Tree):
    def __init__(self):
        self.root = None


    def clear(self):
        """Clear the whole tree"""
        self.root = None


    def insert(self, key, value):
        inserted_node = None
        if self.root is None:
            self.root = Node(key, value)
            inserted_node = self.root
        else:
            inserted_node = self.insert_recursive(key, value, self.root, None, went_left=True)

        return inserted_node


    def insert_recursive(self, key, value, node_input, parent_node, went_left):
        """
        Recursively find where to insert and then insert

        # ARGUMENTS
        key         -> current key
        value       -> current value
        node_input  -> the current node
        parent_node -> the parent node
        went_left   -> True if we went left, False if we went right
        """
        # We found where to insert
        if node_input is None:
            node_input = Node(key=key, value=value)

            # Set parent
            node_input.parent = parent_node
            # Set correct children
            if went_left:
                parent_node.left_child = node_input
            else:
                parent_node.right_child = node_input

            return node_input

        # If we do have a root
        else:
            key_compared = key - node_input.key
            # If it is less than or equal to, go left
            if key_compared <= 0:
                return self.insert_recursive(key, value, node_input.left_child, node_input, went_left=True)
            # If it is greater than, go right
            else:
                return self.insert_recursive(key, value, node_input.right_child, node_input, went_left=False)


    def getValue(self, key):
        start_time = datetime.now().microsecond
        return_node = self.getValueRecursively(key, self.root)
        end_time = datetime.now().microsecond
        print("".join(("Time elapsed: ", str(end_time - start_time), " microseconds")))
        return return_node


    def getValueRecursively(self, key, current_node):
        """Recursively find the key"""
        if current_node is None or current_node.key == key:
            return current_node
        # Go left
        elif key < current_node.key:
            return self.getValueRecursively(key, current_node.left_child)
        # Go right
        elif key > current_node.key:
            return self.getValueRecursively(key, current_node.right_child)


    def printTree(self):
        if self.root is None:
            print("Empty tree!")
        else:
            print("---------------")
            self.printTreeRecursively(self.root, 0, went_left=True)
            print("---------------")


    def printTreeRecursively(self, node_input, indent_value, went_left):
        """Recursively print all the nodes of the tree."""
        if node_input is None:
            return
        else:
            direction = "L" if went_left else "R"
            s = ""
            height = node_input.height
            for i in range(indent_value << 1):
                s = "".join((s, " "))
            s = "".join((s, direction, ". ", str(node_input)))
            print(s)
            self.printTreeRecursively(node_input.left_child, indent_value + 1, went_left=True)
            self.printTreeRecursively(node_input.right_child, indent_value + 1, went_left=False)
