def solution():
    """James drives to Canada at 60 mph.  It is a distance of 360 miles.  He has a 1 hour stop along the way.  How long does he take to get to Canada?"""
    # Define the distance and speed
    distance = 360
    speed = 60

    # Calculate the time taken to travel the distance
    time = distance / speed

    # Add the time taken for the stop
    total_time = time + 1

    # Display the total time taken
    result = total_time
    return result

print(solution())