def solution():
    """Every morning, Carla puts 79 apples in her backpack to eat for lunch. Unfortunately, Buffy stole some of Carla's apples on the school bus, and 26 apples fell out of a hole on the bottom. So at lunchtime, Carla only had 8 apples remaining. How many apples did Buffy steal from Carla?"""
    # Define the initial number of apples
    initial_apples = 79

    # Define the number of apples that were lost
    lost_apples = 26

    # Define the remaining number of apples
    remaining_apples = 8

    # Calculate the number of apples that were stolen
    stolen_apples = initial_apples - remaining_apples - lost_apples

    # Return the result
    result = stolen_apples
    return result

print(solution())