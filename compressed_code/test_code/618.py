def solution():
    
    total_tins = 500
    day_one_tins = 50
    day_two_tins = 3 * day_one_tins
    day_three_tins = day_two_tins - 50
    tins_left = total_tins - day_one_tins - day_two_tins - day_three_tins
    remaining_days = 4
    tins_per_day = tins_left / remaining_days
    result = tins_per_day
    return result

print(solution())