def solution():
    total_distance = 2.5  # Peter has to walk 2.5 miles
    time_per_mile = 20  # It takes Peter 20 minutes to walk one mile
    distance_walked = 1  # Peter has already walked 1 mile
    remaining_distance = total_distance - distance_walked  # Peter has to walk the remaining distance

    # Calculate the time it will take Peter to walk the remaining distance
    remaining_time = remaining_distance * time_per_mile
    result = remaining_time
    return result

print(solution())