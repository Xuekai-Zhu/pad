def solution():
    # Calculate the distance uphill
    uphill_distance = 5 * 0.6  # 60% of the trail is uphill

    # Calculate the distance downhill
    downhill_distance = 5 - uphill_distance

    # Calculate the time taken to travel uphill and downhill
    uphill_time = uphill_distance / 2  # uphill speed is 2 MPH
    downhill_time = downhill_distance / 3  # downhill speed is 3 MPH

    # Calculate the total time taken to travel the trail
    total_time = uphill_time + downhill_time
    total_time_in_minutes = total_time * 60  # convert hours to minutes

    result = total_time_in_minutes
    return result

print(solution())