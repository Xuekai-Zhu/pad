def solution():
    hotdogs_per_minute = 10  # hotdogs eaten by first competitor per minute
    second_competitor = hotdogs_per_minute * 3  # hotdogs eaten by second competitor per minute
    third_competitor = second_competitor * 2  # hotdogs eaten by third competitor per minute
    hotdogs_eaten_by_third_competitor = third_competitor * 5  # hotdogs eaten by third competitor in 5 minutes
    result = hotdogs_eaten_by_third_competitor
    return result

print(solution())