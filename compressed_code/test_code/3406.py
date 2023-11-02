def solution():
    
    hours_per_week = 2 + 1 + 3
    wage_per_week = hours_per_week * 5
    weeks_to_buy_bike = 180 / wage_per_week
    result = weeks_to_buy_bike
    return result

print(solution())