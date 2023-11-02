def solution():
    """I run 12 miles in 90 minutes. What is my average speed in miles per hour?"""
    # Define the distance run and the time taken in minutes
    distance = 12
    time_minutes = 90

    # Convert the time taken to hours
    time_hours = time_minutes / 60

    # Calculate the average speed in miles per hour
    speed = distance / time_hours

    # Return the result
    result = speed
    return result

print(solution())