def solution():
    
    initial_water = 6000
    evaporation = 2000
    drained = 3500
    remaining_water = initial_water - evaporation - drained
    added_rain = 350 * 3
    final_water = remaining_water + added_rain
    result = final_water
    return result

print(solution())