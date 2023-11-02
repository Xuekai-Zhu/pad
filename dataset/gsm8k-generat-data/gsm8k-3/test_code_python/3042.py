def solution():
    """Andy needs to drive from Salt Lake City to Los Angeles. The drive from Salt Lake City to Las Vegas is 420 miles. The drive from Las Vegas to Los Angeles is 273 miles. He wants to make the drive in 11 hours. What's the average minimum speed that Andy needs to drive to reach Los Angeles in 11 hours?"""
    # Define the distances and total time
    distance1 = 420
    distance2 = 273
    total_distance = distance1 + distance2
    total_time = 11

    # Calculate the minimum average speed needed to make the drive in 11 hours
    min_avg_speed = total_distance / total_time

    # Display the minimum average speed
    result = min_avg_speed
    return result

print(solution())