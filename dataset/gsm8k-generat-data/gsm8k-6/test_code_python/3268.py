def solution():
    # Calculate the cost of buying the chocolates
    cost_price = 5 * 5  # $5 each for 5 bars of chocolate

    # Calculate the cost of packaging the chocolate
    packaging_cost = 2 * 5  # $2 for each bar of chocolate

    # Calculate the total cost incurred by Romeo
    total_cost = cost_price + packaging_cost

    # Calculate the profit made by Romeo
    profit = 90 - total_cost
    result = profit
    return result

print(solution())