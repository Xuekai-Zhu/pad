def solution():
    # Calculate the total number of days needed to explore all four islands
    total_days = 1.5 * 4

    # Calculate the total distance they will need to walk for the two islands that require 20 miles per day
    island_1_distance = 20 * total_days
    island_2_distance = 20 * total_days

    # Calculate the total distance they will need to walk for the two islands that require 25 miles per day
    island_3_distance = 25 * total_days
    island_4_distance = 25 * total_days

    # Calculate the total distance they will need to walk
    total_distance = island_1_distance + island_2_distance + island_3_distance + island_4_distance
    result = total_distance
    return result

print(solution())