def solution():
    cost_price = 20  # The store buys the shirt for $20
    profit_percent = 30  # The store charges 30% profit on the cost price
    selling_price = cost_price + (cost_price * profit_percent / 100)  # Calculate the selling price
    sale_percent = 50  # The shirt is on sale for 50% off the selling price
    discounted_price = selling_price - (selling_price * sale_percent / 100)  # Calculate the discounted price
    result = discounted_price
    return result

print(solution())