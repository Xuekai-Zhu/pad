def solution():
    """A man intends to complete a journey of 24 km in 8 hours. If he travels at a speed of 4km/hr for the first four hours, at what speed does he need to travel for the remainder of the journey to be right on time?"""
    # Define the total distance and time
    distance = 24
    time = 8

    # Calculate the distance and time for the first segment of the journey
    distance1 = 4 * 4  # distance = speed * time (4 km/hr for 4 hours)
    time1 = 4

    # Calculate the distance and time for the second segment of the journey
    distance2 = distance - distance1
    time2 = time - time1

    # Calculate the required speed for the second segment of the journey
    speed2 = distance2 / time2

    # Display the required speed for the second segment
    result = speed2
    return result

print(solution())