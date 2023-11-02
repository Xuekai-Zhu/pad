def solution():
    
    potatoes_per_20_minutes = 3
    total_potatoes = 27
    minutes_per_hour = 60
    potatoes_per_hour = (potatoes_per_20_minutes / 20) * minutes_per_hour
    hours_to_eat_all_potatoes = total_potatoes / potatoes_per_hour
    result = hours_to_eat_all_potatoes
    return result

print(solution())