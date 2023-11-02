def solution():
    num_horses = 3 + 5  # 8 horses in total
    drinking_water_per_day = 5  # liters
    bathing_water_per_day = 2  # liters
    num_days = 28

    # Calculate the total amount of drinking water needed for all horses for 28 days
    total_drinking_water = num_horses * drinking_water_per_day * num_days

    # Calculate the total amount of bathing water needed for all horses for 28 days
    total_bathing_water = num_horses * bathing_water_per_day * num_days

    # Calculate the total amount of water needed for all horses for 28 days
    total_water = total_drinking_water + total_bathing_water
    result = total_water
    return result

print(solution())