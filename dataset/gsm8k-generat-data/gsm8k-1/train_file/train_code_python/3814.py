def solution():
    """Richard starts walking from Cincinnati to New York City, which is 70 miles. Richards walks 20 miles the first day.
    The next day he walks 6 miles less than half as much as he walked the first day. He walks 10 miles the third day.
    How many miles further does Richard have to walk to be in New York City?"""
    total_distance = 70
    first_day_distance = 20
    second_day_distance = (first_day_distance / 2) - 6
    third_day_distance = 10
    distance_left = total_distance - (first_day_distance + second_day_distance + third_day_distance)
    result = distance_left
    return result

print(solution())