def solution():
    """A school bus traveled for 42 minutes at a speed of 50 mph. What is the distance the bus traveled in miles?"""
    # Convert the travel time from minutes to hours
    travel_time_hours = 42 / 60

    # Calculate the distance traveled using the formula distance = speed x time
    distance = 50 * travel_time_hours

    # Round the distance to the nearest hundredth
    distance = round(distance, 2)

    # Return the distance traveled
    result = distance
    return result

print(solution())