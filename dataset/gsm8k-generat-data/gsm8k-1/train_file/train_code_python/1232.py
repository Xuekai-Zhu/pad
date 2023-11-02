def solution():
    """Kevin has been for a run and wants to calculate how far he traveled. He ran at 10 miles per hour for half an hour, 20 miles per hour for half an hour, then ran at 8 miles per hour for 15 minutes. How many miles has Kevin run?"""
    half_hour_in_hours = 0.5
    quarter_hour_in_hours = 0.25
    distance_1 = 10 * half_hour_in_hours
    distance_2 = 20 * half_hour_in_hours
    distance_3 = 8 * quarter_hour_in_hours
    total_distance = distance_1 + distance_2 + distance_3
    result = total_distance
    return result

print(solution())