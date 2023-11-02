def solution():
    """Josh wants to build a square sandbox that is 3 ft long, 3 ft wide for his son. He can buy sand in 3 sq ft bags for $4.00 a bag. How much will it cost him to fill up the sandbox?"""
    sandbox_area = 3 * 3
    sandbag_area = 3
    sandbag_cost = 4
    bags_needed = sandbox_area / sandbag_area
    cost = bags_needed * sandbag_cost
    result = cost
    return result

print(solution())