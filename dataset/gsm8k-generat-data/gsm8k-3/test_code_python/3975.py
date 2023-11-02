def solution():
    """Cheryl got angry with her sister and decided to run away from home. She walked 2 miles every hour for 3 hours. Then she got homesick and walked back home. How many miles did Cheryl walk in total?"""
    # Cheryl's first walk
    distance1 = 2 * 3 # distance = speed * time

    # Cheryl's walk back home
    distance2 = 2 * 3 # distance = speed * time

    # Total distance walked
    total_distance = distance1 + distance2
    result = total_distance
    return result

print(solution())