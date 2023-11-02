def solution():
    """Rohan owns a 20-square meter coconut farm. Each square meter has 2 coconut trees and each tree has 6 coconuts. If the coconuts can be harvested every 3 months and each coconut costs $0.50, how much will he earn after 6 months?"""
    # Define the size of the coconut farm
    size = 20

    # Calculate the number of coconut trees on the farm
    trees = size * 2

    # Calculate the total number of coconuts on the farm
    coconuts = trees * 6

    # Calculate the total earnings from harvesting the coconuts every 3 months
    earnings_per_harvest = coconuts * 0.5
    total_earnings = earnings_per_harvest * 2

    # Return the total earnings after 6 months
    result = total_earnings
    return result

print(solution())