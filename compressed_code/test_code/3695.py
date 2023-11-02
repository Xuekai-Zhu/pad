def solution():
    
    night_cost = 1.5
    morning_cost = 2
    night_hours = 6
    morning_hours = 4
    total_cost = (night_cost * night_hours) + (morning_cost * morning_hours)
    money_left = 80 - total_cost
    result = money_left
    return result

print(solution())