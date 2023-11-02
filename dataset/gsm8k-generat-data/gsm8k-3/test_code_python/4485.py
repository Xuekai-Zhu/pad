def solution():
    """Jack bought an ice cream cone before jogging to the beach. If the ice cream cone will melt in 10 minutes, the beach is 16 blocks away, and each block is 1/8th of a mile, how fast does Jack need to jog (in miles per hour) to get to the beach before the ice cream melts?"""
    # Define the distance to the beach in miles
    distance_to_beach = 16 * 1/8

    # Convert the time limit from minutes to hours
    time_limit = 10/60

    # Calculate Jack's required speed in miles per hour
    required_speed = distance_to_beach / time_limit

    # Display Jack's required speed
    result = required_speed
    return result

print(solution())