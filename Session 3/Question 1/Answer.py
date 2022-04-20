number_list = [int(char) for char in input()]

batch_size = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


def find_max(number_list, batch_size):

    max = -1
    index = -1
    for i in range(len(number_list)-batch_size+1):
        product = 1
        for j in range(batch_size):
            product = product * number_list[i + j]
        if product > max:
            max = product
            index = i

    return max, index


def find_min(number_list, batch_size): # finds min product that is not 0

    min = 9999999999
    index = -1
    for i in range(len(number_list)-batch_size+1):
        product = 1
        for j in range(batch_size):
            product = product * number_list[i + j]
        if product != 0 and product < min:
            min = product
            index = i

    return min, index



max, max_index = find_max(number_list, batch_size)

min, min_index = find_min(number_list, batch_size)


print("MAX :", max)
print("NUMBERS :")
for i in range(batch_size):
    print(number_list[max_index + i])
print()
print("MIN :", min)
print("NUMBERS :")
for i in range(batch_size):
    print(number_list[min_index + i])

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
