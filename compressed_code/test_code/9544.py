def solution():
    
    night_rate = 1.5
    morning_rate = 2
    hours_last_night = 6
    hours_this_morning = 4
    total_cost = (night_rate * hours_last_night) + (morning_rate * hours_this_morning)
    money_left = 80 - total_cost
    result = money_left
    return result

print(solution())