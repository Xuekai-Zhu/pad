def solution():
    """Princess Daphne bought three necklaces and a set of earrings for a total of $240,000. If all three necklaces were equal in price, and the earrings were three times as expensive as any one necklace, then how expensive was the cost of a single necklace?"""
    total_cost = 240000
    num_necklaces = 3
    earring_price = 3 * (total_cost / (num_necklaces + 1))
    necklace_price = total_cost / (4 * num_necklaces)
    result = necklace_price
    return result

print(solution())