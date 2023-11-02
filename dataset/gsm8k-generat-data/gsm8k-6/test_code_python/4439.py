def solution():
    cost_price = 20  # cost price of the shirt for the store
    selling_price = cost_price + (0.3 * cost_price)  # selling price with 30% profit
    discounted_price = 0.5 * selling_price  # price after 50% discount
    result = discounted_price
    return result

print(solution())