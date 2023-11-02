def solution():
    """If Ken's house is twice as far from Dawn's house as Mary's house along a certain road, and Ken's house is 4 miles away from Dawn's house along this same road, how much distance (in miles) will Ken cover if he goes from his house to Dawn's house, then Mary's, then back to Dawn's before going back to his own house?"""
    # Define the distance between Ken's house and Dawn's house
    kd_distance = 4

    # Calculate the distance between Mary's house and Ken's house
    mk_distance = kd_distance / 2

    # Calculate the total distance traveled by Ken
    total_distance = kd_distance + mk_distance + kd_distance + mk_distance

    result = total_distance
    return result

print(solution())