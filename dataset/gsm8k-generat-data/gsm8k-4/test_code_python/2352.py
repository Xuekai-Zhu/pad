def solution():
    """James drives to Canada at 60 mph. It is a distance of 360 miles. He has a 1 hour stop along the way. How long does he take to get to Canada?"""
    # Define the distance and speed
    distance = 360
    speed = 60

    # Calculate the time it takes to travel the distance
    travel_time = distance / speed

    # Add the 1 hour stop
    total_time = travel_time + 1

    # Return the result in hours and minutes
    result = "{:.0f} hours and {:.0f} minutes".format(int(total_time), int((total_time % 1) * 60))
    return result

print(solution())