def solution():
    
    tuesday_hours = 5
    wednesday_hours = tuesday_hours * 2
    thursday_hours = wednesday_hours - 2
    total_hours = tuesday_hours + wednesday_hours + thursday_hours
    result = total_hours
    return result

print(solution())