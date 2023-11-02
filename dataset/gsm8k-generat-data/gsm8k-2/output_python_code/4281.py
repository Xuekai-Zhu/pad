def solution():
    """Rohan owns a 20-square meter coconut farm. Each square meter has 2 coconut trees and each tree has 6 coconuts. If the coconuts can be harvested every 3 months and each coconut costs $0.50, how much will he earn after 6 months?"""
    total_trees = 20 * 2
    total_coconuts = total_trees * 6
    six_month_harvest = total_coconuts * 2  # harvest every 3 months for 6 months
    earnings = six_month_harvest * 0.5
    result = earnings
    return result

print(solution())