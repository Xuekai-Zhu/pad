def solution():
    """Mary and Rose went shopping to buy presents. They spent the same amount. Mary bought two pairs of sunglasses for $50 each and a pair of jeans for $100. Rose bought a pair of shoes at $150 and two decks of basketball cards. How much did one deck of basketball cards cost?"""
    mary_total_cost = 2 * 50 + 100
    rose_total_cost = 150 + 2 * x
    total_cost = mary_total_cost  # since the total cost is the same for both
    x = (total_cost - 150) / 2
    result = x
    return result

print(solution())