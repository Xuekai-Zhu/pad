def solution():
    """John gets lost on his way home.  His normal trip is 150 miles and would take him 3 hours.  He ends up driving 50 miles out of the way and has to get back on track.  How long did the trip take if he kept the same speed?"""
    # Define the distance and time for John's normal trip
    DISTANCE = 150
    TIME = 3

    # Define the distance John drove out of the way
    OUT_OF_WAY = 50

    # Calculate the total distance John traveled
    total_distance = DISTANCE + OUT_OF_WAY

    # Calculate the time it took John for the entire trip at the same speed
    time = total_distance / (DISTANCE / TIME)

    # Display the time for the entire trip
    result = time
    return result

print(solution())