def solution():
    """Josh wants to build a square sandbox that is 3 ft long, 3 ft wide for his son. He can buy sand in 3 sq ft bags for $4.00 a bag. How much will it cost him to fill up the sandbox?"""
    length = 3
    width = 3
    area = length * width
    bags_needed = area / 3
    cost_per_bag = 4
    total_cost = bags_needed * cost_per_bag
    result = total_cost
    return result

print(solution())