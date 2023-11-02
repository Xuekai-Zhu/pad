def solution():
    
    first_week_hours = 0
    second_week_hours = 0
    for i in range(14):
        if i < 7:
            first_week_hours += 2
        else:
            second_week_hours += 3
    total_hours = first_week_hours + second_week_hours
    result = total_hours
    return result

print(solution())