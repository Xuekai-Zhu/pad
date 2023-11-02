def solution():
    """Ivar owns a stable. He recently has 3 horses and each horse consumes 5 liters of water for drinking and 2 liters for bathing per day. If he added 5 horses, how many liters of water does Ivar need for all the horses for 28 days?"""
    # Define the number of horses and the amount of water they consume
    num_horses = 8
    drinking_water_per_horse = 5
    bathing_water_per_horse = 2

    # Calculate the total amount of drinking water needed per day
    total_drinking_water_per_day = num_horses * drinking_water_per_horse

    # Calculate the total amount of bathing water needed per day
    total_bathing_water_per_day = num_horses * bathing_water_per_horse

    # Calculate the total amount of water needed per day
    total_water_per_day = total_drinking_water_per_day + total_bathing_water_per_day

    # Calculate the total amount of water needed for 28 days
    total_water_for_28_days = total_water_per_day * 28

    # Return the result
    result = total_water_for_28_days
    return result

print(solution())