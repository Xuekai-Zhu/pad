def solution():
    """Jason has to drive home which is 120 miles away. If he drives at 60 miles per hour for 30 minutes, what speed does he have to average for the remainder of the drive to get there in exactly 1 hour 30 minutes?"""
    # Define the total distance to be covered and the time available to cover it
    total_distance = 120
    total_time = 1.5 # in hours

    # Calculate the time taken for the first half of the journey
    first_half_time = 0.5 # in hours

    # Calculate the distance covered in the first half of the journey
    first_half_distance = 60 * first_half_time

    # Calculate the distance remaining to be covered
    remaining_distance = total_distance - first_half_distance

    # Calculate the time available to cover the remaining distance
    remaining_time = total_time - first_half_time

    # Calculate the average speed required to cover the remaining distance in the remaining time
    remaining_speed = remaining_distance / remaining_time

    # Return the result
    result = remaining_speed
    return result

print(solution())