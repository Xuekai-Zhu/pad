def solution():
    full_distance = 50  # Ezekiel hiked 50 kilometers in three days
    distance_covered = 10 + (full_distance/2)  # Ezekiel covered 10 km on day 1 and half of the full distance on day 2
    remaining_distance = full_distance - distance_covered  # Ezekiel has to cover the remaining distance on day 3
    result = remaining_distance
    return result

print(solution())