def solution():
    num_horses = 3 + 5  # Ivar added 5 horses, so he now has a total of 8
    water_per_horse_per_day = 5 + 2  # each horse needs 5 liters for drinking and 2 liters for bathing
    total_water_per_day = num_horses * water_per_horse_per_day
    total_water_for_28_days = total_water_per_day * 28
    result = total_water_for_28_days
    return result

print(solution())