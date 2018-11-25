import functools


class Tree:
    def __init__(self):
        raise NotImplementedError

    def insert(self, node_input, key, value):
        raise NotImplementedError

    def getValue(self, key):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def printTree(self):
        raise NotImplementedError


@functools.total_ordering
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = None


    def __str__(self):
        s = "Key: " + str(self.key) + ", Value: " + str(self.value) + ", Height: " + str(self.height)
        return s


    def __le__(self, other):
        """Custom defined less than or equal to (LE) function"""
        return self.key <= other.key


    def set_height(self, height):
        """Set the height while storing the old height"""
        old_height = self.height
        self.height = height
        return old_height
