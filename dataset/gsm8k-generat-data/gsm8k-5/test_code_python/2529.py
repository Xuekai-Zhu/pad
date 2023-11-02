def solution():
    hotdogs_per_minute_first = 10  # First competitor can eat 10 hotdogs per minute
    hotdogs_per_minute_second = hotdogs_per_minute_first * 3  # Second competitor can eat 3 times more than first competitor
    hotdogs_per_minute_third = hotdogs_per_minute_second * 2  # Third competitor can eat twice as much as second competitor

    # Calculate the total hotdogs the third competitor can eat in 5 minutes
    total_hotdogs_third = hotdogs_per_minute_third * 5

    result = total_hotdogs_third
    return result

print(solution())