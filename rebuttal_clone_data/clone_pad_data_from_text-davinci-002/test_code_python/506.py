def solution():
    monday_distance = 4.2
    tuesday_distance = 3.8
    wednesday_distance = 3.6
    thursday_distance = 4.4
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance
    days_ran = 4
    result = total_distance / days_ran
    return result

print(solution())