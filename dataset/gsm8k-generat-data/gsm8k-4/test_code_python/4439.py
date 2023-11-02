def solution():
    """Corna wants to buy a shirt. The store buys the shirt for $20, but charges 30% for profit. However, the shirt is on sale for 50% off the selling price. What is the price now?"""
    # Define the cost and profit of the shirt
    cost = 20
    profit_percentage = 30

    # Calculate the selling price of the shirt
    selling_price = cost + (cost * (profit_percentage / 100))

    # Calculate the price of the shirt after the sale
    sale_price = selling_price - (selling_price * 0.5)

    result = sale_price
    return result

print(solution())