def solution():
    
    flat_sand_speed = 60
    downhill_speed = flat_sand_speed + 12
    uphill_speed = flat_sand_speed - 18
    time_on_flat = 1/3
    time_on_downhill = 1/3
    time_on_uphill = 1/3
    average_speed = (flat_sand_speed * time_on_flat) + (downhill_speed * time_on_downhill) + (uphill_speed * time_on_uphill)
    result = average_speed
    return result

print(solution())