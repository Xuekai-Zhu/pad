def solution():
    # Calculate the distance Carson walks in one circle around the warehouse
    distance_per_circle = 2 * (600 + 400)

    # Calculate the total distance Carson should walk
    total_distance = distance_per_circle * 10

    # Calculate the distance Carson skips
    skipped_distance = distance_per_circle * 2

    # Calculate the distance Carson actually walks
    actual_distance = total_distance - skipped_distance
    result = actual_distance
    return result

print(solution())