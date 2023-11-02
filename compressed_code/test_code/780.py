def solution():
    
    water_cooler_size = 3 * 128
    num_chairs = 5 * 10
    water_per_cup = 6
    total_water_needed = num_chairs * water_per_cup
    water_left = water_cooler_size - total_water_needed
    result = water_left
    return result

print(solution())