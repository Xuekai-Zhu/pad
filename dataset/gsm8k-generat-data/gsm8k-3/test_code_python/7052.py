def solution():
    """The average speed for an hour drive is 66 miles per hour. If Felix wanted to drive twice as fast for 4 hours, how many miles will he cover?"""
    # Define the average speed for one hour
    AVERAGE_SPEED = 66

    # Define the number of hours Felix wants to drive for
    hours = 4

    # Calculate Felix's speed for the 4 hour drive
    felix_speed = AVERAGE_SPEED * 2

    # Calculate the distance Felix will cover
    distance = felix_speed * hours

    # Display the distance Felix will cover
    result = distance
    return result

print(solution())