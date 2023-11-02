def solution():
    walk_duration = 1  # hour
    walk_distance = 4  # miles
    num_days = 31  # assuming March has 31 days

    # Calculate the total number of walks Emberly took
    total_walks = num_days - 4  # subtracting 4 days she didn't walk

    # Calculate the total distance Emberly walked
    total_distance = total_walks * walk_duration * walk_distance
    result = total_distance
    return result

print(solution())