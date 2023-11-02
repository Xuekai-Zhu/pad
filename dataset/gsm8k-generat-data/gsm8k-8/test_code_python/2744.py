def solution():
    # Calculate the total distance the potato can be launched
    total_distance = 6 * 200 * 3

    # Convert total distance to feet
    total_distance_feet = total_distance * 3

    # Calculate how long it would take the dog to fetch the potato
    time_to_fetch = total_distance_feet / 400

    result = time_to_fetch / 60
    return result

print(solution())