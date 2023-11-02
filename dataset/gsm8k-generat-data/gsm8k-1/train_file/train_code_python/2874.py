def solution():
    """If Ken's house is twice as far from Dawn's house as Mary's house along a certain road, and Ken's house is 4 miles away from Dawn's house along this same road, how much distance (in miles) will Ken cover if he goes from his house to Dawn's house, then Mary's, then back to Dawn's before going back to his own house?"""
    # Let's assume Mary's house is m miles away from Ken's house.
    # Since Ken's house is twice as far from Dawn's house as Mary's house, Dawn's house must be 2m miles away from Ken's house.
    # Now we know that Ken's house is 4 miles away from Dawn's house.
    # Solving for m, we get: 2m = 4 --> m = 2.
    # So Mary's house is 2 miles away from Ken's house.
    # Therefore, Ken will cover a total distance of:
    total_distance = 4 + 2 + 2 + 2 + 4
    result = total_distance
    return result

print(solution())