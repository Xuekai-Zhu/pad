def solution():
    # Define the original cost and profit margin
    original_cost = 20
    profit_margin = 0.3

    # Calculate the selling price with profit margin
    selling_price = original_cost + (original_cost * profit_margin)

    # Calculate the sale price
    sale_price = selling_price * 0.5

    result = sale_price
    return result

print(solution())