def solution():
    """Jack bought an ice cream cone before jogging to the beach. If the ice cream cone will melt in 10 minutes, the beach is 16 blocks away, and each block is 1/8th of a mile, how fast does Jack need to jog (in miles per hour) to get to the beach before the ice cream melts?"""
    # Define the distance to the beach in miles
    distance = 16 * (1/8)

    # Convert the time in minutes to hours
    time = 10 / 60

    # Calculate the speed needed to reach the beach before the ice cream melts
    speed = distance / time

    # Round the speed to 2 decimal places
    speed = round(speed, 2)

    # return the result in miles per hour
    result = speed
    return result

print(solution())