def solution():
    total_distance = 26
    first_10_miles_time = 1.0  # 1 hour

    remaining_distance = total_distance - 10
    remaining_distance_time = (remaining_distance / 10) * 0.8  # Running at 80% of his pace for remaining distance

    total_time = first_10_miles_time + remaining_distance_time
    result = total_time
    return result

print(solution())