def solution():
    # Calculate the total number of coconut trees
    total_trees = 20 * 2  # Each square meter has 2 trees and Rohan owns a 20-square meter farm

    # Calculate the total number of coconuts Rohan can harvest
    total_coconuts = total_trees * 6  # Each tree has 6 coconuts

    # Calculate the total earnings after 6 months
    earnings_per_harvest = total_coconuts * 0.50  # Each coconut costs $0.50
    total_earnings = earnings_per_harvest * 2  # Rohan can harvest every 3 months, so total of 2 harvests in 6 months

    result = total_earnings
    return result

print(solution())