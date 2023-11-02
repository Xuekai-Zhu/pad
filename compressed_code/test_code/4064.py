def solution():
    
    total_water_allowed = 1000
    water_used_for_drinking_and_cooking = 100
    water_used_for_pool = 10 * 10 * 6
    water_left_for_showers = total_water_allowed - water_used_for_drinking_and_cooking - water_used_for_pool
    showers_can_take = water_left_for_showers / 20
    result = showers_can_take
    return result

print(solution())