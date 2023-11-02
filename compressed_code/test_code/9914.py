def solution():
    
    total_water_allowance = 1000
    water_used_for_drinking_cooking = 100
    water_used_for_pool = 10 * 10 * 6
    water_remaining = total_water_allowance - water_used_for_drinking_cooking - water_used_for_pool
    water_per_shower = 20
    showers_possible = water_remaining / water_per_shower
    result = int(showers_possible)
    return result

print(solution())