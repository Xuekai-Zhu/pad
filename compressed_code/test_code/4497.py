def solution():
    
    corn_plants = 4 * 15
    corn_water_needed = corn_plants * 0.5
    pig_water_needed = 10 * 4
    duck_water_needed = 20 * 0.25
    total_water_needed = corn_water_needed + pig_water_needed + duck_water_needed
    pump_speed = 3
    pumping_time = total_water_needed / pump_speed
    result = pumping_time
    return result

print(solution())