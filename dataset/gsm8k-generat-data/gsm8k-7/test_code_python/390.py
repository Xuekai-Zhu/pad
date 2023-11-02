def solution():
    starting_distance = 2
    target_distance = 20
    increment = 2/3

    # Calculate the total distance Oscar needs to run
    total_distance = target_distance - starting_distance

    # Calculate the number of weeks needed to reach the target distance
    num_weeks = total_distance / increment

    result = num_weeks
    return result

print(solution())