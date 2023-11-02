def solution():
    """Peter and Andrew like to run in the morning. Peter runs 3 miles more than Andrew's 2 miles. After 5 days, how many miles have they both run?"""
    # Define the distance Andrew runs each day
    andrew_distance = 2

    # Define the distance Peter runs each day
    peter_distance = andrew_distance + 3

    # Calculate the total distance both of them run in a day
    total_distance = andrew_distance + peter_distance

    # Calculate the total distance both of them run in 5 days
    total_distance_5_days = total_distance * 5

    # Return the result
    result = total_distance_5_days
    return result

print(solution())