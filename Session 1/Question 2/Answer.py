map_size = int(input())
amount_of_water = int(input())
water_index = int(input())
total_steps = int(input())
water_change_div = int(input())


def print_map(map):
    for element in map:
        print("{:.2f}".format(element), end=" ")
    print()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

map = [0] * map_size
new_map = [0] * map_size



map[water_index] = amount_of_water
new_map[water_index] = amount_of_water

print("START")
print_map(map)

for step in range(total_steps):
    print("STEP", step + 1)

    if map[0] > map[1]:
        change = (map[0] - map[1]) / water_change_div
        new_map[1] = new_map[1] + change
        new_map[0] = new_map[0] - change

    for i in range(1, map_size-1):
        if map[i] > map[i - 1]:
            change = (map[i] - map[i - 1]) / water_change_div
            new_map[i - 1] = new_map[i - 1] + change
            new_map[i] = new_map[i] - change
        if map[i] > map[i + 1]:
            change = (map[i] - map[i + 1]) / water_change_div
            new_map[i + 1] = new_map[i + 1] + change
            new_map[i] = new_map[i] - change

    if map[map_size-1] > map[map_size-2]:
        change = (map[map_size-1] - map[map_size-2]) / water_change_div
        new_map[map_size-2] = new_map[map_size-2] + change
        new_map[map_size-1] = new_map[map_size-1] - change


    for i in range(map_size):
        map[i] = new_map[i]

    print_map(map)


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE



