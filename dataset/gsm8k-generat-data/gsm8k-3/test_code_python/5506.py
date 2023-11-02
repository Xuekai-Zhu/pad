def solution():
    """The first tank is 300 liters filled while the second tank is 450 liters filled. The second tank is only 45% filled. If the two tanks have the same capacity, how many more liters of water are needed to fill the two tanks?"""
    # Define the capacities of the two tanks
    TANK_CAPACITY = 450

    # Calculate the volume of water in the second tank
    second_tank_volume = 450 * 0.45

    # Calculate the volume of water in the first tank
    first_tank_volume = 300

    # Calculate the total volume of water in the two tanks
    total_volume = first_tank_volume + second_tank_volume

    # Calculate the amount of water needed to fill up both tanks
    water_needed = 2 * TANK_CAPACITY - total_volume

    # Display the amount of water needed
    result = water_needed
    return result

print(solution())