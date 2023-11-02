def solution():
    
    starting_chickens = 4
    final_chickens = starting_chickens * 8
    eggs_per_chicken_per_day = 6
    total_eggs_per_day = final_chickens * eggs_per_chicken_per_day
    eggs_per_week = total_eggs_per_day * 7
    result = eggs_per_week
    return result

print(solution())