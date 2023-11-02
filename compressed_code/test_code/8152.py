def solution():
    
    tank_capacity = 50 * 1000 
    rain_collect = 800
    river_collect = 1700
    total_collect_per_day = rain_collect + river_collect
    days_to_fill_tank = tank_capacity // total_collect_per_day
    result = days_to_fill_tank
    return result

print(solution())