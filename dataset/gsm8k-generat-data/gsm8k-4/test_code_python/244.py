def solution():
    """A fox can run at the maximum speed of 50 kilometers per hour. Considering the fox would run at a constant speed, what distance would he make during 120 minutes?"""
    # Convert minutes to hours
    time_hours = 120/60

    # Calculate the distance traveled at maximum speed
    distance = 50 * time_hours

    result = distance
    return result

print(solution())