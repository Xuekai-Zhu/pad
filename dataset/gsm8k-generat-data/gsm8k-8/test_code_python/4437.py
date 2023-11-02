def solution():
    # Calculate the total distance of this year's race
    race_distance = 300 * 4

    # Calculate the total number of intervals between the tables
    num_intervals = 6 - 1

    # Calculate the distance between each interval
    interval_distance = race_distance / num_intervals

    # Calculate the distance between table 1 and table 3
    distance_between_1_and_3 = interval_distance * 2

    result = distance_between_1_and_3
    return result

print(solution())