def solution():
    """Last week, the price of a movie ticket was $100. This year the price is down by 20%. What's the new price of the movie ticket?"""
    original_price = 100
    percent_decrease = 20
    decrease_amount = original_price * (percent_decrease / 100)
    new_price = original_price - decrease_amount
    result = new_price
    return result

print(solution())