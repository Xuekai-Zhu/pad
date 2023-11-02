def solution():
    # Calculate the total number of trees
    total_trees = 20 * 2

    # Calculate the total number of coconuts
    total_coconuts = total_trees * 6

    # Calculate the total earnings for one harvest
    earnings_per_harvest = total_coconuts * 0.50

    # Calculate the total earnings for two harvests
    total_earnings = earnings_per_harvest * 2

    result = total_earnings
    return result

print(solution())