def solution():
    """Bob's school track is 400 meters. If Bob ran the first lap in 70 seconds, the second and third lap in 85 seconds each, what was his average speed in (m/s) for his entire run?"""
    total_distance = 3 * 400
    total_time = 70 + 85 + 85
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())