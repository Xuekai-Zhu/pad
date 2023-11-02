def solution():
    pairs_per_hour = 3
    hours_mon_thu = 8 * 4
    hours_fri = 3
    total_hours = hours_mon_thu + hours_fri

    # Calculate the total number of pairs of shoes that can be mended in a week
    total_pairs = pairs_per_hour * total_hours
    result = total_pairs
    return result

print(solution())