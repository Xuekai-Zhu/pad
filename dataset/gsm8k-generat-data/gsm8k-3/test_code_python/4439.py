def solution():
    """Corna wants to buy a shirt. The store buys the shirt for $20, but charges 30% for profit. However, the shirt is on sale for 50% off the selling price. What is the price now?"""
    # Define the cost and profit percentage of the shirt
    cost = 20
    profit_percentage = 0.3

    # Calculate the selling price of the shirt
    selling_price = cost * (1 + profit_percentage)

    # Calculate the sale price of the shirt
    sale_price = selling_price * 0.5

    # Display the sale price
    result = sale_price
    return result

print(solution())