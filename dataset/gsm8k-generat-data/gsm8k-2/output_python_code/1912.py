def solution():
    """If farmer Steven can use his tractor to plow up to 10 acres of farmland per day, or use the same tractor to mow up to 12 acres of grassland per day, how long would it take him to plow his 55 acres of farmland and mow his 30 acres of grassland?"""
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