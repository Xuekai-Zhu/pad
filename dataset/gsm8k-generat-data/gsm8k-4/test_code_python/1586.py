def solution():
    """Emma traveled by car 280 miles in 2 hours 20 minutes. What was the average speed of the car in miles per hour?"""
    # Define the distance and time traveled
    distance = 280
    time_hours = 2 + 20/60

    # Calculate the average speed
    average_speed = distance / time_hours

    # Return the result
    result = average_speed
    return result

print(solution())