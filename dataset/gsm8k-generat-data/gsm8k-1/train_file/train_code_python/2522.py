def solution():
    """Jim buys a wedding ring for $10,000. He gets his wife a ring that is twice that much and sells the first one for half its value. How much is he out of pocket?"""
    wedding_ring_price = 10000
    wife_ring_price = wedding_ring_price * 2
    sold_first_ring_price = wedding_ring_price / 2
    total_spent = wedding_ring_price + wife_ring_price - sold_first_ring_price
    result = total_spent
    return result

print(solution())