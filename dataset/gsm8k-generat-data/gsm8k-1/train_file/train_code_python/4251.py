def solution():
    """Maria bought a ticket to a ZOO. The regular price stands at $15, but she was able to get a 40% discount. How much did Maria pay for the ticket?"""
    regular_price = 15
    discount_percent = 40
    discount_amount = regular_price * (discount_percent / 100)
    sale_price = regular_price - discount_amount
    result = sale_price
    return result

print(solution())