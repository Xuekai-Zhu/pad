def solution():
    """To make 3 km, Ben walked for 2 hours. Continuing at the same speed, how much time in minutes would it take him to travel 12 km?"""
    # Define the distance and time values for the first part of the trip
    distance_1 = 3
    time_1 = 2

    # Calculate the speed for the first part of the trip
    speed = distance_1 / time_1

    # Define the distance value for the second part of the trip
    distance_2 = 12

    # Calculate the time for the second part of the trip
    time_2 = distance_2 / speed

    # Convert the time to minutes
    time_2_minutes = time_2 * 60

    # Return the result
    result = time_2_minutes
    return result

print(solution())