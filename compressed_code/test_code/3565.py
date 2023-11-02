def solution():
    
    first_weeks = 3
    second_weeks = first_weeks + 2
    last_weeks = 2 * second_weeks
    total_weeks = first_weeks + second_weeks + last_weeks
    total_days = total_weeks * 7
    result = total_days
    return result

print(solution())