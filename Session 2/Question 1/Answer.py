hours_to_complete = [int(x) for x in input().split(" ")]

hours_spent_pd = [int(x) for x in input().split(" ")]

days = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


# There is an easier solution but this is probably what most of the students will try to do
completed = [0] * len(hours_to_complete)
tmp_timings = hours_to_complete.copy()

for _ in range(days):
    print("DAY", _ + 1)
    for i in range(len(tmp_timings)):
        tmp_timings[i] = tmp_timings[i] - hours_spent_pd[i]
        if tmp_timings[i] <= 0:
            tmp_timings[i] = tmp_timings[i] + hours_to_complete[i]
            completed[i] = completed[i] + 1
    print(completed)



print("TOTAL TIME SPENT :", days * sum(hours_spent_pd))
print("TOTAL JOBS COMPLETED :", sum(completed))
print("MOST COMPLETED JOB :", completed.index(max(completed)), max(completed))
print("LEAST COMPLETED JOB :", completed.index(min(completed)), min(completed))

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE