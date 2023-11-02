def solution():
    """Bill and Ted went into the forest to gather some wild mushrooms. Bill gathered 12 red mushrooms and 6 brown mushrooms. Ted gathered 14 green mushrooms and 6 blue mushrooms. If half of the blue mushrooms, two-thirds of the red mushrooms, and all of the brown mushrooms have white spots, how many white-spotted mushrooms did they gather?"""
    red_with_spots = 12 * (2/3)
    brown_with_spots = 6
    blue_with_spots = 6 * (1/2)
    
    total_with_spots = red_with_spots + brown_with_spots + blue_with_spots
    result = total_with_spots
    return result

print(solution())