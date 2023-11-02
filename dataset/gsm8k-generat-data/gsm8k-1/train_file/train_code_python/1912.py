def solution():
    """If farmer Steven can use his tractor to plow up to 10 acres of farmland per day, or use the same tractor to mow up to 12 acres of grassland per day, how long would it take him to plow his 55 acres of farmland and mow his 30 acres of grassland?"""
    farmland_total = 55
    grassland_total = 30
    farmland_plowed_per_day = 10
    grassland_mowed_per_day = 12
    
    days_to_plow_farmland = farmland_total // farmland_plowed_per_day
    days_to_mow_grassland = grassland_total // grassland_mowed_per_day
    
    total_days = days_to_plow_farmland + days_to_mow_grassland
    
    result = total_days
    
    return result

print(solution())