def solution():
    
    rolls_of_toilet_paper = 1000
    squares_per_roll = 300
    daily_use = 3 * 5
    total_squares_used_per_day = daily_use
    total_squares = rolls_of_toilet_paper * squares_per_roll
    days_supply = total_squares / total_squares_used_per_day
    result = days_supply
    return result

print(solution())