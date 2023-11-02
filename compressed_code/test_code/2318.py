def solution():
    
    tank_size = 50
    rain_water = 0.8 
    river_water = 1.7 
    daily_water = rain_water + river_water
    days_to_fill = tank_size / daily_water
    result = days_to_fill
    return result

print(solution())