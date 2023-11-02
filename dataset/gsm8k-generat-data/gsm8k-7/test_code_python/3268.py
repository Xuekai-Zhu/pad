def solution():
    num_bars = 5
    bar_cost = 5
    total_income = 90
    packaging_cost = 2

    # Calculate the total cost of buying all the bars of chocolate
    total_cost = num_bars * (bar_cost + packaging_cost)

    # Calculate the profit made from selling all the bars of chocolate
    total_profit = total_income - total_cost
    result = total_profit
    return result

print(solution())