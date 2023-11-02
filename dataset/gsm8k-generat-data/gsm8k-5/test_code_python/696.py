def solution():
    starting_apples = 79  # Carla starts with 79 apples
    lost_apples = 26  # Some apples were lost on the bus
    remaining_apples = 8  # Carla only had 8 apples left at lunchtime

    # Calculate how many apples Buffy stole
    stolen_apples = starting_apples - remaining_apples - lost_apples
    result = stolen_apples
    return result

print(solution())