def solution():
    miles_per_day1 = 20  # The first set of islands require walking 20 miles per day
    miles_per_day2 = 25  # The second set of islands require walking 25 miles per day
    days_per_island = 1.5  # It takes 1.5 days to explore each island
    num_islands1 = 2  # There are two islands that require walking 20 miles per day
    num_islands2 = 2  # There are two islands that require walking 25 miles per day

    # Calculate the total distance walked for the first set of islands
    total_distance1 = miles_per_day1 * days_per_island * num_islands1

    # Calculate the total distance walked for the second set of islands
    total_distance2 = miles_per_day2 * days_per_island * num_islands2

    # Calculate the total distance walked for all islands
    total_distance = total_distance1 + total_distance2
    result = total_distance
    return result

print(solution())