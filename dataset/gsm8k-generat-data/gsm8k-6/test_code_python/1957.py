def solution():
    # Calculate the total revenue from selling newspapers
    total_revenue = 500 * 2 * 0.8  # He sells 80% of 500 newspapers for $2 each

    # Calculate the cost of buying the newspapers
    cost = 500 * 2 * 0.25  # He buys the newspapers for 75% less than the selling price

    # Calculate the profit
    profit = total_revenue - cost
    result = profit
    return result

print(solution())