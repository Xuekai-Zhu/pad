def solution():
    books_prices = [25.00, 18.00, 21.00, 35.00, 12.00, 10.00]
    total_cost = 0

    # Calculate the cost of the books over $22 with 30% discount
    for price in books_prices:
        if price > 22:
            total_cost += price * 0.7
        elif price < 20:
            total_cost += price * 0.8
        else:
            total_cost += price

    result = total_cost
    return result

print(solution())