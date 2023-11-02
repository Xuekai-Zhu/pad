def solution():
    """Roger rode his bike for 2 miles this morning, and then 5 times that amount in the evening. How many miles did Roger ride his bike for?"""
    morning_distance = 2
    evening_distance = 5 * morning_distance
    total_distance = morning_distance + evening_distance
    result = total_distance
    return result

print(solution())