def solution():
    prices = [25.00, 18.00, 21.00, 35.00, 12.00, 10.00]  # prices of books
    total_cost = 0  # total cost before discounts

    # Calculate total cost before discounts
    for price in prices:
        if price > 22.00:
            total_cost += price
        elif price < 20.00:
            total_cost += price * 0.8
        else:
            total_cost += price * 0.7

    result = total_cost
    return result

print(solution())