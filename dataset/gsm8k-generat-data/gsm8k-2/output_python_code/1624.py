def solution():
    """Last week, the price of a movie ticket was $100. This year the price is down by 20%. What's the new price of the movie ticket?"""
    original_price = 100
    discount = 0.2
    new_price = original_price - (original_price * discount)
    result = new_price
    return result

print(solution())