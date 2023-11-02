def solution():
    
    num_men = 25
    water_per_man_per_day = 0.5
    num_days = 4000 / 200
    total_water_needed = num_men * water_per_man_per_day * num_days
    result = total_water_needed
    return result

print(solution())