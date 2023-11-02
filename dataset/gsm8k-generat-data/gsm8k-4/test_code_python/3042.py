def solution():
    """Andy needs to drive from Salt Lake City to Los Angeles. The drive from Salt Lake City to Las Vegas is 420 miles. The drive from Las Vegas to Los Angeles is 273 miles. He wants to make the drive in 11 hours. What's the average minimum speed that Andy needs to drive to reach Los Angeles in 11 hours?"""
    # Define the distances
    distance_slc_lv = 420
    distance_lv_la = 273

    # Define the total time available for the trip
    total_time = 11

    # Calculate the time spent driving from Salt Lake City to Las Vegas
    time_slc_lv = distance_slc_lv / 60

    # Calculate the remaining time available for the trip
    remaining_time = total_time - time_slc_lv

    # Calculate the minimum average speed needed for the remaining distance
    minimum_speed = distance_lv_la / (remaining_time / 60)

    # Return the result
    result = minimum_speed
    return result

print(solution())