def solution():
    """Ivar owns a stable. He recently has 3 horses and each horse consumes 5 liters of water for drinking and 2 liters for bathing per day. If he added 5 horses, how many liters of water does Ivar need for all the horses for 28 days?"""
    num_horses = 8
    water_for_drinking = 5
    water_for_bathing = 2
    water_per_horse_per_day = water_for_drinking + water_for_bathing
    total_water_per_day = num_horses * water_per_horse_per_day
    total_water_for_28_days = total_water_per_day * 28
    result = total_water_for_28_days
    return result

print(solution())