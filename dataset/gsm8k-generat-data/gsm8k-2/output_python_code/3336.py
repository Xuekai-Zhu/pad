def solution():
    """Bill gathered 12 red mushrooms and 6 brown mushrooms. Ted gathered 14 green mushrooms and 6 blue mushrooms. If half of the blue mushrooms, two-thirds of the red mushrooms, and all of the brown mushrooms have white spots, how many white-spotted mushrooms did they gather?"""
    red_spotted = 2/3 * 12
    brown_spotted = 6
    blue_spotted = 1/2 * 6
    total_spotted = red_spotted + brown_spotted + blue_spotted
    result = total_spotted
    return result

print(solution())