def solution():
    """Ivar owns a stable. He recently has 3 horses and each horse consumes 5 liters of water for drinking and 2 liters for bathing per day.
     If he added 5 horses, how many liters of water does Ivar need for all the horses for 28 days?"""
    num_horses = 8
    drinking_water_per_day = 5
    bathing_water_per_day = 2
    total_water_per_day = (drinking_water_per_day + bathing_water_per_day) * num_horses
    total_water_for_28_days = total_water_per_day * 28
    result = total_water_for_28_days
    return result

print(solution())