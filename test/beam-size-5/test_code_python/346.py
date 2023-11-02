def solution():
    
    monday_hours = 1
    tuesday_hours = monday_hours * 3
    wednesday_hours = tuesday_hours / 2
    thursday_hours = tuesday_hours / 2
    friday_hours = 2
    total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours + friday_hours
    result = total_hours
    return result

print(solution())