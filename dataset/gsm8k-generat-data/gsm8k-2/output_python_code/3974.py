def solution():
    """Cheryl got angry with her sister and decided to run away from home. She walked 2 miles every hour for 3 hours. Then she got homesick and walked back home. How many miles did Cheryl walk in total?"""
    distance_per_hour = 2
    hours = 3
    one_way_distance = distance_per_hour * hours
    total_distance = one_way_distance * 2
    result = total_distance
    return result

print(solution())