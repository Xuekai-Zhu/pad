def solution():
    
    total_water = 60
    water_on_other_days = 9*3 + 8*3 
    water_on_wednesday = total_water - water_on_other_days 
    result = water_on_wednesday
    return result

print(solution())