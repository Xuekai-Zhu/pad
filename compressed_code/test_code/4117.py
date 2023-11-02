def solution():
    
    wednesday_hours = 2
    thursday_hours = 2
    friday_hours = wednesday_hours + 3

    total_hours = wednesday_hours + thursday_hours + friday_hours
    average_hours = total_hours / 3
    result = average_hours
    return result

print(solution())