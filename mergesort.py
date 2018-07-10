from random import randint


# Merge based on indices
def merge_two_sorted_lists(left_list, right_list):
    len_left_list = len(left_list)
    len_right_list = len(right_list)
    total_len = len(left_list) + len(right_list)
    merged_list = [0] * total_len
    index1 = 0
    index2 = 0
    merge_index = 0

    while (index1 < len_left_list or index2 < len_right_list):
        # put the rest of right_list onto the merged list
        if (index1 >= len_left_list):
            merged_list[merge_index] = right_list[index2]
            merge_index += 1
            index2 += 1
        # put the rest of left_list onto the merged list
        elif (index2 >= len_right_list):
            merged_list[merge_index] = left_list[index1]
            merge_index += 1
            index1 += 1
        # sort!
        else:
            # left_list < right_list
            if (left_list[index1] <= right_list[index2]):
                temp_int = left_list[index1]
                index1 += 1
            else:
                temp_int = right_list[index2]
                index2 += 1
            merged_list[merge_index] = temp_int
            merge_index += 1

    return merged_list


def merge_sort(input_list):
    left_index = 0
    right_index = len(input_list) - 1

    # If there are two or less elements, return the list
    if (right_index - left_index <= 1):
        # if there are two or more elements, sort them
        if (right_index >= 1):
            if (input_list[right_index] < input_list[left_index]):
                temp = input_list[right_index]
                input_list[right_index] = input_list[left_index]
                input_list[left_index] = temp

        return input_list

    # More than one element per list
    middle_index = (right_index + left_index) >> 1  # divide by 2

    left_half = merge_sort(input_list[0:middle_index])  # sort the left half
    right_half = merge_sort(input_list[middle_index:(right_index + 1)])  # sort the right half

    return merge_two_sorted_lists(left_half, right_half)  # merge the two halves


# left_list = [2, 4, 6, 8]
# right_list = [3, 5, 7]
# merged_list = merge_two_sorted_lists(left_list, right_list)
# print(merged_list)

num_elems = randint(15, 25)
print("num_elems: {}".format(num_elems))
unsorted_list = [randint(0, 10) for i in range(num_elems)]

print(unsorted_list)
print(len(unsorted_list))
sorted_list = merge_sort(unsorted_list)
print(sorted_list)
print(len(sorted_list))
