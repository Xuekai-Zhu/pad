def solution():
    """Richard starts walking from Cincinnati to New York City, which is 70 miles. Richards walks 20 miles the first day. The next day he walks 6 miles less than half as much as he walked the first day. He walks 10 miles the third day. How many miles further does Richard have to walk to be in New York City?"""
    total_distance = 70
    distance_day1 = 20
    distance_day2 = (0.5 * distance_day1) - 6
    distance_day3 = 10
    distance_covered = distance_day1 + distance_day2 + distance_day3
    remaining_distance = total_distance - distance_covered
    result = remaining_distance
    return result

print(solution())