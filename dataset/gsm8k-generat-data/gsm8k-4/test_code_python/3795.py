def solution():
    """If Natasha was going 10 mph over the speed limit and it took her an hour to arrive at her destination that was 60 miles away, what was the speed limit?"""
    # Define the distance and time of the trip
    distance = 60
    time = 1

    # Calculate the actual speed of Natasha during the trip
    actual_speed = distance / time

    # Calculate the speed limit by subtracting 10 from the actual speed
    speed_limit = actual_speed - 10

    # return the result
    result = speed_limit
    return result

print(solution())