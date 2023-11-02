def solution():
    """Ivar owns a stable. He recently has 3 horses and each horse consumes 5 liters of water for drinking and 2 liters for bathing per day. If he added 5 horses, how many liters of water does Ivar need for all the horses for 28 days?"""
    # Define the number of horses and water consumption per horse
    HORSES = 3
    DRINKING_WATER = 5
    BATHING_WATER = 2

    # Define the number of new horses
    NEW_HORSES = 5

    # Define the number of days
    DAYS = 28

    # Calculate the total water consumption per horse per day
    total_water_per_horse = DRINKING_WATER + BATHING_WATER

    # Calculate the total water consumption for all the horses per day
    total_water_per_day = HORSES * total_water_per_horse

    # Calculate the total water consumption for all the horses and new horses for the given number of days
    total_water = (HORSES + NEW_HORSES) * total_water_per_horse * DAYS

    # Display the total water consumption
    result = total_water
    return result

print(solution())