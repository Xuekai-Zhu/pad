def solution():
    """James buys 3 shirts for $60. There is a 40% off sale. How much did he pay per shirt after the discount?"""
    original_price = 60 / 3  # $20 per shirt
    discount_percentage = 40
    discounted_price = original_price * (1 - discount_percentage/100)
    result = discounted_price
    return result

print(solution())