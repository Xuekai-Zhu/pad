def solution():
    starting_distance = 3 # miles
    additional_distance_per_week = 1 # mile
    num_weeks = 5

    # Calculate the total additional distance Jackson will run over the next four weeks
    total_additional_distance = additional_distance_per_week * (num_weeks - 1)

    # Calculate the total distance Jackson will run over the five weeks (including the first week)
    total_distance = starting_distance + total_additional_distance

    # Calculate the average distance Jackson will run per day over the five weeks
    average_distance_per_day = total_distance / 35 # 35 days in total

    result = average_distance_per_day
    return result

print(solution())