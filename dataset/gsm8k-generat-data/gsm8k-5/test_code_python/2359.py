def solution():
    cost_per_orange = 12.50 / 25  # Joshua paid $12.50 for 25 oranges, so cost per orange is $0.50
    selling_price_per_orange = 0.60  # Joshua is selling each orange for 60 cents

    # Calculate the profit in cents per orange
    profit_per_orange = (selling_price_per_orange - cost_per_orange) * 100
    result = profit_per_orange
    return result

print(solution())