def solution():
    """If Ken's house is twice as far from Dawn's house as Mary's house along a certain road, and Ken's house is 4 miles away 
    from Dawn's house along this same road, how much distance (in miles) will Ken cover if he goes from his house to Dawn's 
    house, then Mary's, then back to Dawn's before going back to his own house?"""
    ken_mary_distance = 4
    ken_dawn_distance = 2 * ken_mary_distance
    total_distance = ken_dawn_distance + ken_mary_distance + ken_dawn_distance + ken_mary_distance
    result = total_distance
    return result

print(solution())