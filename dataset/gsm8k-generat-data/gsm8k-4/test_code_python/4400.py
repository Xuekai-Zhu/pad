def solution():
    """Roberto is out for a hike. He travels uphill at 2 MPH and downhill at 3MPH. The trail is 5 miles long. 60% is uphill and the rest is downhill. How long does it take him to complete it in minutes?"""
    # Define the uphill and downhill distances
    uphill_distance = 5 * 0.6
    downhill_distance = 5 - uphill_distance

    # Calculate the time taken to travel uphill and downhill
    uphill_time = uphill_distance / 2
    downhill_time = downhill_distance / 3

    # Calculate the total time taken for the entire trail
    total_time = uphill_time + downhill_time

    # Convert the time to minutes
    total_time_minutes = total_time * 60

    # Round the result to the nearest minute
    result = round(total_time_minutes)
    return result

print(solution())