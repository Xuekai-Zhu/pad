def solution():
    """Lexi wants to run a total of three and one-fourth miles. One lap on a particular outdoor track measures a quarter of a mile around. How many complete laps must she run?"""
    total_distance = 3.25
    lap_distance = 0.25
    laps_required = total_distance / lap_distance
    result = int(laps_required)
    return result

print(solution())