def solution():
    cost_price = 20
    profit_percentage = 0.3
    discount_percentage = 0.5

    # Calculate the selling price with profit
    selling_price = cost_price + (cost_price * profit_percentage)

    # Calculate the discounted selling price
    discounted_price = selling_price * (1 - discount_percentage)

    result = discounted_price
    return result

print(solution())