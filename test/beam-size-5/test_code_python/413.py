def solution():
    
    first_four_days_distance = 200 * 4
    next_two_days_distance = 0.3 * first_four_days_distance
    total_distance = first_four_days_distance + next_two_days_distance
    second_week_days_distance = 300 * 2
    total_distance = total_distance + second_week_days_distance
    result = total_distance
    return result

print(solution())