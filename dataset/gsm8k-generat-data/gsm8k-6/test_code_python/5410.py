def solution():
    # Calculate the time it takes to hike the first trail
    time_first_trail = 20 / 5  # James can cover it at 5 miles per hour

    # Calculate the time it takes to hike the second trail
    time_second_trail = (6 + 6) / 3  # James can only cover 3 miles per hour and takes an hour break halfway through

    # Calculate the difference in time between the two trails
    time_difference = time_second_trail - time_first_trail

    result = time_difference
    return result

print(solution())