def solution():
    
    pill_box_capacity = 7 * 2
    bottle_1 = 120
    bottle_2 = 120
    bottle_3 = 120
    bottle_4 = 30
    bottle_5 = 30
    total_pills = bottle_1 + bottle_2 + bottle_3 + bottle_4 + bottle_5
    pills_per_day = 5
    pills_per_week = pills_per_day * 7
    pills_for_two_weeks = pills_per_week * 2
    total_pills_used = pills_for_two_weeks
    total_pills_left = total_pills - total_pills_used
    result = total_pills_left
    return result

print(solution())