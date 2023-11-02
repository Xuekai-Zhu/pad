def solution():
    """Emberly takes her mornings walks every day. If each walk takes her 1 hour covering 4 miles, and she didn't walk for 4 days in March, calculate the total number of miles she's walked."""
    walk_time = 1
    walk_distance = 4
    days_not_walked = 4
    days_walked = 31 - days_not_walked
    total_distance = days_walked * walk_time * walk_distance
    result = total_distance
    return result

print(solution())