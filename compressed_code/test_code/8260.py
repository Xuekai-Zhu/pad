def solution():
    
    water_goal = 100
    water_bottle_size = 12
    refills = 7
    total_water_consumed = water_bottle_size * refills
    remaining_water_needed = water_goal - total_water_consumed
    result = remaining_water_needed
    return result

print(solution())