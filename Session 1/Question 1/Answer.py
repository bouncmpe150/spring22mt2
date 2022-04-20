
unsorted_list = [int(x) for x in input().split(" ")]

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

for i in range(len(unsorted_list)):

    min_index = i
    for j in range(i + 1, len(unsorted_list)):
        if unsorted_list[min_index] > unsorted_list[j]:
            min_index = j

    unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

print(unsorted_list)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE