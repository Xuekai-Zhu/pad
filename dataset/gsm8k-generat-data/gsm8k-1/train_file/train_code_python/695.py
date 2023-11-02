def solution():
    """Every morning, Carla puts 79 apples in her backpack to eat for lunch. Unfortunately, Buffy stole some of Carla's apples on the school bus, and 26 apples fell out of a hole on the bottom. So at lunchtime, Carla only had 8 apples remaining. How many apples did Buffy steal from Carla?"""
    starting_apples = 79
    apples_lost = 26
    remaining_apples = 8
    apples_stolen = starting_apples - remaining_apples - apples_lost
    result = apples_stolen
    return result

print(solution())