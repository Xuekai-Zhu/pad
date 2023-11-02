def solution():
    num_horses = 3  # Ivar has 3 horses
    water_per_horse = 5 + 2  # Each horse consumes 5 liters for drinking and 2 liters for bathing
    total_water_per_day = num_horses * water_per_horse  # Total water consumed by all the horses per day

    # If Ivar adds 5 more horses, the total number of horses will be:
    total_horses = num_horses + 5

    # Calculate the total water consumed by all the horses for 28 days
    total_water_28_days = total_water_per_day * total_horses * 28

    result = total_water_28_days
    return result

print(solution())