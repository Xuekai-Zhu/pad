def solution():
    
    cow_count = 40
    cow_water_per_day = 80
    cow_water_per_week = cow_count * cow_water_per_day * 7

    sheep_count = cow_count * 10
    sheep_water_per_day = cow_water_per_day * 0.25
    sheep_water_per_week = sheep_count * sheep_water_per_day * 7

    total_water_per_week = cow_water_per_week + sheep_water_per_week
    result = total_water_per_week
    return result

print(solution())