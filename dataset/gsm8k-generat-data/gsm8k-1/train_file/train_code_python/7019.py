def solution():
    """Emberly takes her mornings walks every day. If each walk takes her 1 hour covering 4 miles, and she didn't walk for 4 days in March, calculate the total number of miles she's walked."""
    distance_per_walk = 4
    walks_per_day = 1
    days_in_March = 31
    days_walked = days_in_March - 4
    total_distance = distance_per_walk * walks_per_day * days_walked
    result = total_distance
    return result

print(solution())