def solution():
    """Princess Daphne bought three necklaces and a set of earrings for a total of $240,000. If all three necklaces were equal in price, and the earrings were three times as expensive as any one necklace, then how expensive was the cost of a single necklace?"""
    total_cost = 240000
    num_necklaces = 3
    earrings_cost = 3.0  # earrings are three times expensive as one necklace
    cost_per_necklace = (total_cost - (earrings_cost * cost_per_necklace)) / num_necklaces
    result = cost_per_necklace
    return result

print(solution())