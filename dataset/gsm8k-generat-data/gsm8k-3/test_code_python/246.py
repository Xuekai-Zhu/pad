def solution():
    """A fox can run at the maximum speed of 50 kilometers per hour. Considering the fox would run at a constant speed, what distance would he make during 120 minutes?"""
    # Define the fox's maximum speed in kilometers per minute
    FOX_SPEED_KM_PER_MINUTE = 50 / 60

    # Define the time in minutes
    time_in_minutes = 120

    # Calculate the distance the fox would make during the given time
    distance = FOX_SPEED_KM_PER_MINUTE * time_in_minutes

    # Display the distance
    result = distance
    return result

print(solution())