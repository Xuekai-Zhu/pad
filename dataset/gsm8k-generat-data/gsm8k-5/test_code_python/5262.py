def solution():
    distance_covered = 5 * 3  # Fabian covered a total distance of 15 kilometers
    remaining_distance = 30 - distance_covered  # Fabian has to cover the remaining distance
    remaining_time = remaining_distance / 5  # Fabian walks 5 kilometers every hour

    result = remaining_time
    return result

print(solution())