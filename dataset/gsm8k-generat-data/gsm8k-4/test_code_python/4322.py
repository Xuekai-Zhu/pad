def solution():
    """Melinda is taking a 1200-mile trip with her family to visit their cousins. How much time will they save if they drive 60 miles an hour instead of 50 miles an hour?"""
    # Define the distance of the trip and the two different speeds
    distance = 1200
    speed1 = 50
    speed2 = 60

    # Calculate the time it would take to complete the trip at each speed
    time1 = distance / speed1
    time2 = distance / speed2

    # Calculate the time saved by driving at the faster speed
    time_saved = time1 - time2

    # Return the time saved
    result = time_saved
    return result

print(solution())