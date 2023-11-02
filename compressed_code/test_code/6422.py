def solution():
    
    total_tins = 500
    first_day = 50
    second_day = 3 * first_day
    third_day = second_day - 50
    tins_left = total_tins - first_day - second_day - third_day
    remaining_days = 4
    tins_per_day = tins_left / remaining_days
    result = tins_per_day
    return result

print(solution())