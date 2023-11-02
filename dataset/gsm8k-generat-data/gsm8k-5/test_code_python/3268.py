def solution():
    cost_price = 5 + 2  # Each bar of chocolate costs him $5 and $2 for packaging
    selling_price = 90 / 5  # He sold all five bars of chocolate for a total of $90

    # Calculate Romeo's profit
    total_profit = (selling_price - cost_price) * 5
    result = total_profit
    return result

print(solution())