def solution():
    """Jason has to drive home which is 120 miles away. If he drives at 60 miles per hour for 30 minutes, what speed does he have to average for the remainder of the drive to get there in exactly 1 hour 30 minutes?"""
    # Convert 30 minutes to 0.5 hours
    initial_time = 0.5

    # Convert 1 hour 30 minutes to 1.5 hours
    final_time = 1.5

    # Define the distance of the drive
    distance = 120

    # Calculate the remaining time for the drive
    remaining_time = final_time - initial_time

    # Calculate the remaining distance for the drive
    remaining_distance = distance - (60 * initial_time)

    # Calculate the required average speed for the remaining distance
    required_speed = remaining_distance / remaining_time

    # Display the required average speed
    result = required_speed
    return result

print(solution())