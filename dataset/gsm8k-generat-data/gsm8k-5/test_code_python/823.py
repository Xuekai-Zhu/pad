def solution():
    starting_apples = 74  # At the beginning of the day, there were 74 apples in the basket
    ricki_removes = 14  # Ricki removes 14 apples
    samson_removes = 2 * ricki_removes  # Samson removes twice as many apples as Ricki

    # Calculate the total number of apples removed
    total_removed = ricki_removes + samson_removes

    # Calculate the number of apples left in the basket by the end of the day
    apples_left = starting_apples - total_removed
    result = apples_left
    return result

print(solution())