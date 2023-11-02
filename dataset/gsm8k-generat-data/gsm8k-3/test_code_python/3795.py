def solution():
    """If Natasha was going 10 mph over the speed limit and it took her an hour to arrive at her destination that was 60 miles away, what was the speed limit?"""
    # Set the distance and time variables
    distance = 60
    time = 1

    # Calculate the actual speed using the given information
    actual_speed = distance / time

    # Calculate the speed limit by subtracting 10 mph from the actual speed
    speed_limit = actual_speed - 10

    # Display the speed limit
    result = speed_limit
    return result

print(solution())