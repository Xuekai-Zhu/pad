def solution():
    """Rohan owns a 20-square meter coconut farm. Each square meter has 2 coconut trees and each tree has 6 coconuts. If the coconuts can be harvested every 3 months and each coconut costs $0.50, how much will he earn after 6 months?"""
    # Calculate the total number of coconut trees
    total_trees = 20 * 2

    # Calculate the total number of coconuts
    total_coconuts = total_trees * 6

    # Calculate the total earnings in 3 months
    earnings_3_months = total_coconuts * 0.5

    # Calculate the total earnings in 6 months
    earnings_6_months = earnings_3_months * 2

    # Display the total earnings
    result = earnings_6_months
    return result

print(solution())