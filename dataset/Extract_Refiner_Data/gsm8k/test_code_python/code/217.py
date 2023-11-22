def solution():
    
    initial_water = 120
    used_water = 90
    remaining_water = initial_water - used_water
    rainwater = remaining_water * 2
    total_water = remaining_water + rainwater
    result = total_water
    return result

print(solution())