def solution():
    """Jim buys a wedding ring for $10,000. He gets his wife a ring that is twice that much and sells the first one for half its value. How much is he out of pocket?"""
    first_ring_cost = 10000
    second_ring_cost = 2 * first_ring_cost
    sold_ring_value = 0.5 * first_ring_cost
    total_cost = second_ring_cost - sold_ring_value
    result = total_cost
    return result

print(solution())