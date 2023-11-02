def solution():
    # Calculate the total distance Jamie walks (3 miles with group + 2 miles per day for 6 days)
    jamie_total_distance = 3 + (2 * 6)

    # Calculate the total distance Sue walks (0.5 miles per day * 6 days)
    sue_total_distance = 0.5 * 6

    # Calculate the total distance the group walks (3 miles)
    group_total_distance = 3

    # Calculate the total distance walked by all the ladies
    total_distance = (jamie_total_distance + sue_total_distance + group_total_distance) * 6

    result = total_distance
    return result

print(solution())