def solution():
    distance_per_day = 10
    num_days = 80

    # Calculate the total distance driven in one day
    total_distance_per_day = distance_per_day * 2

    # Calculate the total distance driven in the semester
    total_distance = total_distance_per_day * num_days
    result = total_distance
    return result

print(solution())