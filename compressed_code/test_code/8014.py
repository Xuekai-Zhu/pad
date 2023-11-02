def solution():
    
    old_average = 3
    monday_time = 2
    tuesday_time = 4
    wednesday_time = 3
    thursday_time = 4
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time
    friday_time = (old_average * 5) - total_time
    result = friday_time
    return result

print(solution())