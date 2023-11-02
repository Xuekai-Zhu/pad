def solution():
    """Cindy can run at 3 miles per hour and walk at 1 mile per hour. If she runs for half a mile and then walks for half a mile, how many minutes will it take her to travel the full mile?"""
    # Define Cindy's speeds
    RUN_SPEED = 3
    WALK_SPEED = 1

    # Define the distance Cindy travels
    distance = 1

    # Calculate the time it takes Cindy to run and walk the distance
    time = (0.5 / RUN_SPEED) + (0.5 / WALK_SPEED)

    # Convert the time to minutes
    time_minutes = time * 60

    # Display the time in minutes
    result = time_minutes
    return result

print(solution())