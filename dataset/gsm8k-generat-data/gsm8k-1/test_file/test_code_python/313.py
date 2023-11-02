def solution():
    """John fills a 6 foot by 4 foot pool that is 5 feet deep. It cost $.1 per cubic foot to fill. How much does it cost to fill?"""
    length = 6
    width = 4
    depth = 5
    cubic_feet = length * width * depth
    cost_per_cubic_foot = 0.1
    total_cost = cubic_feet * cost_per_cubic_foot
    result = total_cost
    return result

print(solution())