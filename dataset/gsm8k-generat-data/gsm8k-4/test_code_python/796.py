def solution():
    """Carla can cook a batch of waffles in 10 minutes and chicken-fried steak in 6 minutes. How long will it take her to cook 3 steaks and a batch of waffles?"""
    # Define the time it takes to cook waffles and steak
    WAFFLES_TIME = 10
    STEAK_TIME = 6

    # Calculate the total time it takes to cook 3 steaks
    total_steak_time = 3 * STEAK_TIME

    # Calculate the total time it takes to cook waffles and 3 steaks
    total_time = WAFFLES_TIME + total_steak_time

    result = total_time
    return result

print(solution())