def solution():
    # Calculate the total number of coconut trees and coconuts in the farm
    num_trees = 20 * 2  # 2 coconut trees for every 1 square meter of land
    num_coconuts = num_trees * 6  # 6 coconuts for every 1 coconut tree

    # Calculate the total earnings after 6 months
    total_earnings = (num_coconuts * 0.50) * 2  # harvest every 3 months, so twice in 6 months
    result = total_earnings
    return result

print(solution())