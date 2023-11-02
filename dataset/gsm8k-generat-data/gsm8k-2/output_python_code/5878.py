def solution():
    """Jean the jaguar has a beautiful fur coat containing a pattern of many rose-shaped spots, as unique as a human fingerprint. Half of her spots are located on her upper torso, with one-third of the spots located on her back and hindquarters, and the remaining spots located on her sides. If Jean has 30 spots on her upper torso, how many spots does she have located on her sides?"""
    total_spots = 30 * 2  # double the spots on the upper torso
    back_spots = total_spots / 3
    torso_spots = 30
    side_spots = total_spots - back_spots - torso_spots
    result = side_spots
    return result

print(solution())