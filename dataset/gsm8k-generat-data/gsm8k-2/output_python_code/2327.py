def solution():
    """I bought a pair of shoes for $51. The shoes were already marked 75% off. What is the original price of the shoes?"""
    sale_price = 51
    discount = 0.75
    original_price = sale_price / (1 - discount)
    result = original_price
    return result

print(solution())