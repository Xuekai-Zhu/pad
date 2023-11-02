def solution():
    target_distance = 20  # Oscar wants to run a 20-mile marathon
    starting_distance = 2  # Oscar has already run 2 miles
    added_distance_per_week = 2/3  # Oscar plans to add 2/3 miles per week

    # Calculate the remaining distance Oscar needs to add to reach the target distance
    remaining_distance = target_distance - starting_distance

    # Calculate the number of weeks Oscar needs to train at the given pace
    weeks = remaining_distance / added_distance_per_week
    result = weeks
    return result

print(solution())