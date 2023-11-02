def solution():
    """Kevin has been for a run and wants to calculate how far he traveled. He ran at 10 miles per hour for half an hour, 20 miles per hour for half an hour, then ran at 8 miles per hour for 15 minutes. How many miles has Kevin run?"""
    time_1 = 0.5
    time_2 = 0.5
    time_3 = 0.25
    distance_1 = 10 * time_1
    distance_2 = 20 * time_2
    distance_3 = 8 * time_3
    total_distance = distance_1 + distance_2 + distance_3
    result = total_distance
    return result

print(solution())