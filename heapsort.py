"""
    Heap sort algorithm using a max heap.

    Author: Todd Nguyen
    Last Updated: Monday July 9, 2018 at 10:23 (24h time)
"""

from random import randint


def heap_sort(input_list):
    """
    Sort a list using a max heap.

    # Arguments
    input_list -- The list to be sorted.
    """
    cur_max_index = len(input_list) - 1
    # Build a max heap
    heapify(input_list, max_heap=True)

    while (cur_max_index >= 0):
        # Swap the 0th index element with the current last element
        temp_num = input_list[0]
        input_list[0] = input_list[cur_max_index]
        input_list[cur_max_index] = temp_num

        # Decrement our index/current max heap length
        cur_max_index -= 1

        # Heap property is destroyed, thus we must sift down
        # We have to add 1 to the end index as we must pass the current length of
        # the input list to the sift_down function
        sift_down(input_list, end_index=cur_max_index + 1, cur_node_index=0, max_heap=True)


def find_index_parent(cur_index):
    """
    Find the index of the parent node.

    # Arguments:
    cur_index -- the index of the current node

    """
    return (cur_index - 1) >> 1  # parent index is floor((i - 1) / 2)


def find_index_left_child(cur_index):
    """
    Find the index of the left child node.

    # Arguments:
    cur_index -- the index of the current node

    """

    return cur_index * 2 + 1


def find_index_right_child(cur_index):
    """
    Find the index of the right child node.

    # Arguments:
    cur_index -- the index of the current node

    """

    return cur_index * 2 + 2


def sift_down(input_list, end_index, cur_node_index, max_heap=True):
    """
    Move the current node to its appropriate position

    # Arguments
    input_list      -- The list of inputs.
    cur_node_index  -- The index of the current node being looked at
    max_heap        -- True if a max heap is being built, False for a min heap.
                       (Default = True)

    """

    heap_len = end_index
    index_left = find_index_left_child(cur_node_index)
    index_right = find_index_right_child(cur_node_index)
    wanted_index = cur_node_index  # the largest/smallest index

    # If it is a max heap
    if (max_heap):
        # Check against the left child. We want the parent node to be larger than the children node
        if (index_left < heap_len) and (input_list[index_left] > input_list[wanted_index]):
            wanted_index = index_left
        # Check against the right child. We want the parent node to be larger than the children node
        if (index_right < heap_len) and (input_list[index_right] > input_list[wanted_index]):
            wanted_index = index_right
    # If it is a min_heap
    else:
        # Check against the left child. We want the parent node to be smaller than the children node
        if (index_left < heap_len) and (input_list[index_left] < input_list[wanted_index]):
            wanted_index = index_left
        # Check against the right child. We want the parent node to be smaller than the children node
        if (index_right < heap_len) and (input_list[index_right] < input_list[wanted_index]):
            wanted_index = index_right

    # If we changed the wanted_index, that means that we have found a new
    # index for our current node
    if (wanted_index != cur_node_index):
        # We will swap the current node with its corresponding child
        temp_num = input_list[wanted_index]
        input_list[wanted_index] = input_list[cur_node_index]
        input_list[cur_node_index] = temp_num
        # Recursively call the function again
        sift_down(input_list=input_list, end_index=heap_len, cur_node_index=wanted_index, max_heap=max_heap)


def heapify(input_list, max_heap=True):
    """
    Build a max/min help from an input list in a bottom-up manner.

    # Arguments
    input_list  -- The list of inputs.
    max_heap    -- True if you want a max heap, False if you want a min heap
    """

    heap_len = len(input_list)
    # Since it is bottom up, we will start from the halfway point (heap_len / 2),
    # all the way to the first index
    cur_index = heap_len >> 1
    while (cur_index >= 0):
        sift_down(input_list=input_list, end_index=len(input_list),
                  cur_node_index=cur_index, max_heap=max_heap)
        cur_index -= 1


def check_correct_heap(heap_input, max_heap):
    """
    Check if the heap is correctly sorted.

    # Arguments:
    heap_input  -- The heap to be checked
    max_heap    -- If the heap is a max heap or a min heap. True for max heap,
                   False for a min heap
    """

    heap_len = len(heap_input)
    # We only have to look at half of the list since the other half does
    # not have children
    for i in range(heap_len >> 1):
        index_left_child = i * 2 + 1
        index_right_child = i * 2 + 2

        # Check the current node against its children
        # Check for max heap
        if max_heap:
            if index_left_child < heap_len and heap_input[i] < heap_input[index_left_child]:
                return False
            if index_right_child < heap_len and heap_input[i] < heap_input[index_right_child]:
                return False
        # Check for min heap
        else:
            if index_left_child < heap_len and heap_input[i] > heap_input[index_left_child]:
                return False
            if index_left_child < heap_len and heap_input[i] > heap_input[index_right_child]:
                return False

    return True


def sample():
    """
    Sample inputs that can be ran.
    """
    max_int = randint(6, 10)
    is_max_heap = True
    input_list = [randint(0, 10) for i in range(max_int)]
    input_list_copy = input_list.copy()
    print(input_list)
    print("Heaped? {}".format(check_correct_heap(input_list, max_heap=is_max_heap)))
    heapify(input_list, max_heap=is_max_heap)
    print(input_list)
    print("Heaped? {}".format(check_correct_heap(input_list, max_heap=is_max_heap)))

    heap_sort(input_list_copy)
    print("\n{}\n".format(input_list_copy))

    blah = [9, 7, 6, 4, 7, 2, 0, 4, 2, 6]
    heap_sort(blah)
    print(blah)
