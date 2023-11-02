def solution():
    
    farmland_size = 55
    grassland_size = 30
    plow_speed = 10
    mow_speed = 12
    total_plow_days = farmland_size / plow_speed
    total_mow_days = grassland_size / mow_speed
    total_days = total_plow_days + total_mow_days
    result = total_days
    return result

print(solution())