def solution():
    
    total_hours = 7
    monday_hours = 1
    tuesday_hours = 1
    wednesday_hours = 1
    thursday_hours = 1
    thursday_hours = 2
    friday_hours = 2
    monday_30min = monday_hours * 30
    tuesday_30min = tuesday_hours * 30
    wednesday_30min = wednesday_hours * 30
    thursday_30min = thursday_hours * 30
    friday_30min = friday_hours * 30
    total_30min = monday_30min + tuesday_30min + wednesday_30min + thursday_30min + friday_30min
    result = total_30min
    return result

print(solution())