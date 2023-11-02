def solution():
    """You can lower the price by 20% if you buy more than fifteen units of iPhone cases. If you pay $500 to buy 18 units, what is the original price?"""
    units_purchased = 18
    discounted_price = 500
    original_price = discounted_price / ((100 - 20) / 100) / units_purchased
    result = original_price
    return result

print(solution())