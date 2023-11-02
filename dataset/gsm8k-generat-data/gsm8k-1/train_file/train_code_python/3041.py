def solution():
    """Andy needs to drive from Salt Lake City to Los Angeles. The drive from Salt Lake City to Las Vegas is 420 miles. The drive from Las Vegas to Los Angeles is 273 miles. He wants to make the drive in 11 hours. What's the average minimum speed that Andy needs to drive to reach Los Angeles in 11 hours?"""
    total_distance = 420 + 273
    total_time = 11
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())