def solution():
    distance_covered_by_amoli = 42 * 3  # Amoli drove 42 miles an hour for 3 hours
    distance_covered_by_anayet = 61 * 2  # Anayet drove at 61 miles an hour for 2 hours

    # Total distance covered by both
    total_distance_covered = distance_covered_by_amoli + distance_covered_by_anayet

    # Distance left to travel
    distance_left = 369 - total_distance_covered
    result = distance_left
    return result

print(solution())