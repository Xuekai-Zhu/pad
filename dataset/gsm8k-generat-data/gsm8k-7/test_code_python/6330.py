def solution():
    total_distance = 50
    first_day_distance = 10
    second_day_distance = total_distance / 2

    # Calculate the total distance covered on the first two days
    total_covered_distance = first_day_distance + second_day_distance

    # Calculate the remaining distance to be covered on the third day
    remaining_distance = total_distance - total_covered_distance
    result = remaining_distance
    return result

print(solution())