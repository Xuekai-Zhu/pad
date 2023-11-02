def solution():
    length = 600
    width = 400
    num_circles = 10
    num_skips = 2

    # Calculate the total distance Carson would walk if he completed all circles
    total_distance = 2 * (length + width) * num_circles

    # Calculate the distance Carson skipped
    skip_distance = 2 * (length + width) * num_skips

    # Calculate the actual distance Carson walked
    actual_distance = total_distance - skip_distance
    result = actual_distance
    return result

print(solution())