def solution():
    product_cost = 90  # cost of the product to Bert from the warehouse
    selling_price = product_cost + 10  # selling price in Bert's shop
    tax = 0.1  # 10% tax on each sale

    # Calculate Bert's profit from the sale
    profit = selling_price * (1 - tax) - product_cost
    result = profit
    return result

print(solution())