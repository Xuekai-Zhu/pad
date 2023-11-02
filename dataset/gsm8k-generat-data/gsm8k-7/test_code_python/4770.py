def solution():
    night_cost = 1.5
    morning_cost = 2.0
    num_hours_last_night = 6
    num_hours_this_morning = 4
    total_hours = num_hours_last_night + num_hours_this_morning
    total_cost = (num_hours_last_night * night_cost) + (num_hours_this_morning * morning_cost)
    remaining_money = 80 - total_cost
    result = remaining_money
    return result

print(solution())