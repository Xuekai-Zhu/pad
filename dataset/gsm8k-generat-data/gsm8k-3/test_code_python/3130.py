def solution():
    """Jace drives 60 miles per hour. If Jace drives for 4 hours straight, take a 30-minute break, and then drives for another 9 hours straight, how many miles will he travel?"""
    # Define Jace's speed in miles per hour
    SPEED = 60

    # Define Jace's driving time in hours
    driving_time = 4 + 9

    # Define Jace's break time in hours
    break_time = 0.5

    # Calculate the total distance Jace will travel
    total_distance = SPEED * (driving_time + break_time)

    # Display the total distance
    result = total_distance
    return result

print(solution())