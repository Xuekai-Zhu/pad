def solution():
    """Carla can cook a batch of waffles in 10 minutes and chicken-fried steak in 6 minutes. How long will it take her to cook 3 steaks and a batch of waffles?"""
    # Define the time it takes to cook a batch of waffles and a chicken-fried steak
    WAFFLE_TIME = 10
    STEAK_TIME = 6

    # Calculate the total time it takes to cook 3 steaks and a batch of waffles
    total_time = (3 * STEAK_TIME) + WAFFLE_TIME

    # Display the total time
    result = total_time
    return result

print(solution())