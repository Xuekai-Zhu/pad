def solution():
    
    
    
    num_helium_balloons = 1800 / 50
    
    
    num_air_balloons = 50 - num_helium_balloons
    
    
    num_touch_ceiling = num_helium_balloons
    
    
    num_not_touch_ceiling = num_air_balloons
    
    
    difference = num_touch_ceiling - num_not_touch_ceiling
    
    result = difference
    
    return result

print(solution())