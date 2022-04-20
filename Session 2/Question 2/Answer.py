file_name = input()
product = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

info_file = open(file_name, 'r')
info = info_file.readlines()

found = False

for line in info:
    l = line.split('\t')
    if product == l[0]:
        price = 1
        for i in range(2, 7):
            price *= float(l[i])
        found = True
        print("%.2f" % price)
        # print(price)
        break
        
if not found:
    print("No product found")

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE ../testcases/prices.txt