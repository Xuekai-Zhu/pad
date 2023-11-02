def solution():
    """Dennis wants to buy 4 pairs of pants from the store which cost $110.00 each with a 30% discount and he also wants to buy 2 pairs of socks which cost $60.00 with a 30% discount. How much money will Dennis have to spend in total after he bought all the items he wants after the discount?"""
    pants_price = 110
    socks_price = 60
    pants_discount = 0.3
    socks_discount = 0.3
    total_pants_price = pants_price * 4 * (1 - pants_discount)
    total_socks_price = socks_price * 2 * (1 - socks_discount)
    total_price = total_pants_price + total_socks_price
    result = total_price
    return result

print(solution())