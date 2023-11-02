def solution():
    monday_time = 2
    tuesday_time = 4
    wednesday_time = 3
    thursday_time = 4
    old_average = 3
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time
    desired_average = old_average
    friday_time = (4 * desired_average) - total_time
    result = friday_time
    return result

print(solution())