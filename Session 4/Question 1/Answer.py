
n_of_days = int(input())

temperatures = [int(x) for x in input().split(" ")]

clothing = [int(x) for x in input().split(" ")]

medicine = [eval(x) for x in input().split(" ")]

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

risk = []

streak = 0
will_be_sick = False
for i in range(n_of_days):
    if ((temperatures[i] <= 15 and clothing[i] <= 4) or (temperatures[i] > 25 and clothing[i] > 7)) and (not medicine[i]):
        risk.append(True)
        streak = streak + 1
    else:
        risk.append(False)
        streak = 0
    if streak == 2:
        will_be_sick = True


print(risk)
print(will_be_sick)


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
