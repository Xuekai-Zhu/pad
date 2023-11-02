def solution():
    time_per_mile_without_brother = 9
    time_per_mile_with_brother = 12
    distance = 20

    # Calculate the time it would take Derek to walk 20 miles without his brother
    time_without_brother = time_per_mile_without_brother * distance

    # Calculate the time it would take Derek to walk 20 miles with his brother
    time_with_brother = time_per_mile_with_brother * distance

    # Calculate the difference in time between the two scenarios
    time_difference = time_with_brother - time_without_brother
    result = time_difference
    return result

print(solution())