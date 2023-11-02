def solution():
    books_prices = [25, 18, 21, 35, 12, 10]
    total_cost = 0

    for price in books_prices:
        if price > 22:
            total_cost += price * 0.7  # 30% discount
        elif price < 20:
            total_cost += price * 0.8  # 20% discount
        else:
            total_cost += price

    result = total_cost
    return result

print(solution())