def solution():
    """Roberto is out for a hike. He travels uphill at 2 MPH and downhill at 3MPH. The trail is 5 miles long. 60% is uphill and the rest is downhill. How long does it take him to complete it in minutes?"""
    # Define the length of the entire trail
    trail_length = 5

    # Calculate the length of the uphill and downhill sections of the trail
    uphill_length = trail_length * 0.6
    downhill_length = trail_length - uphill_length

    # Calculate the time it takes to travel uphill and downhill
    uphill_time = uphill_length / 2
    downhill_time = downhill_length / 3

    # Calculate the total time it takes Roberto to complete the trail
    total_time = uphill_time + downhill_time

    # Convert the total time to minutes
    total_time_minutes = total_time * 60

    # Display the total time in minutes
    result = total_time_minutes
    return result

print(solution())