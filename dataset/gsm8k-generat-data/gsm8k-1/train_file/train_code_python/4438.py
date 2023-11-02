def solution():
    """Corna wants to buy a shirt. The store buys the shirt for $20, but charges 30% for profit. However, the shirt is on sale for 50% off the selling price. What is the price now?"""
    cost_price = 20
    profit_percentage = 30
    selling_price = cost_price + (cost_price * (profit_percentage / 100))
    discount_percentage = 50
    discounted_price = selling_price - (selling_price * (discount_percentage / 100))
    result = discounted_price
    return result

print(solution())