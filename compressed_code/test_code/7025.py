def solution():
    
    monday_hours = 4
    tuesday_hours = monday_hours - 2
    wednesday_hours = monday_hours * 2
    thursday_hours = tuesday_hours * 2
    total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours
    result = total_hours
    return result

print(solution())