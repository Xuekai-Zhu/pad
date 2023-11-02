def solution():
    """The average speed for an hour drive is 66 miles per hour. If Felix wanted to drive twice as fast for 4 hours, how many miles will he cover?"""
    original_speed = 66
    faster_speed = 2 * original_speed
    time = 4
    distance_at_original_speed = original_speed * time
    distance_at_faster_speed = faster_speed * time
    total_distance = distance_at_original_speed + distance_at_faster_speed
    result = total_distance
    return result

print(solution())