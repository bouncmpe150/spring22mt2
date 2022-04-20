file_name = input()
employee = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

info_file = open(file_name, 'r')
info = info_file.readlines()

found = False

for line in info:
    l = line.split('\t')
    if employee == l[1]:
        sum_male = 0
        sum_female = 0
        for i in range(11, 18, 2):
            sum_male += float(l[i])
            sum_female += float(l[i+1])
        print("%.2f" % ((sum_male - sum_female) / 4))
        found = True
        break

if not found:
    print("No employee found")
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE