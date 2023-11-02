def solution():
    """A desert garden's sprinkler system runs twice a day during the cool morning and evening hours. It waters the garden with four liters of water in the morning and six liters in the evening. How many days does it take the sprinkler system to use 50 liters of water?"""
    # Define the amount of water used in each cycle
    MORNING_WATER = 4
    EVENING_WATER = 6

    # Define the total amount of water needed
    TOTAL_WATER = 50

    # Calculate the number of cycles needed to use the total amount of water
    total_cycles = TOTAL_WATER / (MORNING_WATER + EVENING_WATER)

    # Calculate the number of days needed for the total amount of water
    total_days = total_cycles / 2

    # Display the number of days needed
    result = total_days
    return result

print(solution())