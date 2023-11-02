def solution():
    
    men = 25
    water_per_day_per_man = 0.5
    water_per_day = men * water_per_day_per_man
    distance_per_day = 200
    total_distance = 4000
    days = total_distance / distance_per_day
    total_water = days * water_per_day
    result = total_water
    return result

print(solution())