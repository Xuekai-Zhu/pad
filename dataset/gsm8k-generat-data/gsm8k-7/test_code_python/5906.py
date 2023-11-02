def solution():
    num_teammates = 4
    distance_per_teammate = 3
    distance_ratio = 2

    # Calculate the total distance covered by all teammates
    total_teammate_distance = num_teammates * distance_per_teammate

    # Calculate the distance covered by Ralph
    ralph_distance = distance_ratio * distance_per_teammate

    # Calculate the total distance of the race
    total_distance = total_teammate_distance + ralph_distance
    result = total_distance
    return result

print(solution())